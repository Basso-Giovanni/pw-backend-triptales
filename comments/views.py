from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .helpers import assert_user_can_comment_post
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        assert_user_can_comment_post(self.request.user, post_id)
        return Comment.objects.filter(post__id=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        post_id = self.kwargs['post_pk']
        assert_user_can_comment_post(self.request.user, post_id)
        serializer.save(author=self.request.user, post_id=post_id)

class CommentDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        assert_user_can_comment_post(self.request.user, post_id)
        return Comment.objects.filter(post__id=post_id)

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied("Non puoi eliminare questo commento.")
        instance.delete()

