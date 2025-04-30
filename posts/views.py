from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer

class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.created_by:
            raise PermissionDenied("Non puoi modificare questo post.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.created_by:
            raise PermissionDenied("Non puoi eliminare questo post.")
        instance.delete()


# SEZIONE DI CODICE PER IL LIKE DEI POST
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.likes.add(request.user)
    return Response({'status': 'liked'})

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.likes.remove(request.user)
    return Response({'status': 'unliked'})

# SEZIONE DI CODICE PER CLASSIFICA POST

class TopLikedPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return Post.objects.filter(group_id=group_id) \
            .annotate(likes_count=Count('likes')) \
            .order_by('-likes_count', '-created_at')

# SEZIONE DI CODICE PER CLASSIFICA UTENTI

User = get_user_model()

class UserTopLikesView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, group_id):
        # Aggrega like ricevuti per autore nei post di quel gruppo
        user_likes = (
            User.objects.filter(created_posts__group_id=group_id)
            .annotate(total_likes=Count('created_posts__likes', distinct=True))
            .filter(total_likes__gt=0)  # esclude chi ha 0 like
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
