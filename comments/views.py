from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        return Comment.objects.filter(post__id=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        post_id = self.kwargs['post_pk']
        serializer.save(author=self.request.user, post_id=post_id)

class CommentDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        return Comment.objects.filter(post__id=post_id)

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied("Non puoi eliminare questo commento.")
        instance.delete()

