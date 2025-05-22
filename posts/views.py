from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from trips.badge_utils import check_and_assign_user_badge
from .helpers import assert_user_is_group_member
from .models import Post
from .serializers import PostSerializer

User = get_user_model()

#per creare un post
class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        group = serializer.validated_data.get('group')
        assert_user_is_group_member(self.request.user, group.id)
        serializer.save(created_by=self.request.user)
        check_and_assign_user_badge(self.request.user, group)

#per vedere/aggiornare/cancellare i dettagli di un post
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.created_by:
            raise PermissionDenied("Non puoi modificare questo post.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.created_by:
            raise PermissionDenied("Non puoi eliminare questo post.")
        instance.delete()

# SEZIONE DI CODICE PER IL LIKE DEI POST
#per mettere like ad un post
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    assert_user_is_group_member(request.user, post.group.id)
    post.likes.add(request.user)
    check_and_assign_user_badge(request.user, post.group)

    return Response({'status': 'liked'})

#per togliere il like
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = Post.objects.get(pk=pk)
    assert_user_is_group_member(request.user, post.group.id)
    post.likes.remove(request.user)
    return Response({'status': 'unliked'})

#classifica post
class TopLikedPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        assert_user_is_group_member(self.request.user, group_id)
        return Post.objects.filter(group_id=group_id) \
            .annotate(likes_count=Count('likes')) \
            .order_by('-likes_count', '-created_at')

#classifica utenti (like)
class UserTopLikesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, group_id):
        assert_user_is_group_member(self.request.user, group_id)
        user_likes = (
            User.objects.filter(created_posts__group_id=group_id)
            .annotate(total_likes=Count('created_posts__likes'))
            .filter(total_likes__gt=0)  #ignora chi non ha like
            .order_by('-total_likes')
        )

        data = [
            {
                'user_id': user.id,
                'username': user.username,
                'total_likes': user.total_likes
            }
            for user in user_likes
        ]
        return Response(data)

#classifica utenti (post)
class UserTopPostsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, group_id):
        assert_user_is_group_member(self.request.user, group_id)
        # conta i post per utente
        user_post_counts = (
            User.objects.filter(created_posts__group_id=group_id)
            .annotate(total_posts=Count('created_posts'))
            .filter(total_posts__gt=0)
            .order_by('-total_posts')
        )

        data = [
            {
                'user_id': user.id,
                'username': user.username,
                'total_posts': user.total_posts
            }
            for user in user_post_counts
        ]
        return Response(data)
