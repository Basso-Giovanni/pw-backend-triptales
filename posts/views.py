from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
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