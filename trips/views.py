from rest_framework import generics, permissions, status
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer
from .helpers import assert_user_is_group_member
from .models import TripGroup
from .serializers import TripGroupSerializer

class CreateTripGroupView(generics.CreateAPIView):
    queryset = TripGroup.objects.all()
    serializer_class = TripGroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, members=[self.request.user])


class JoinTripGroupView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TripGroupSerializer

    def post(self, request, *args, **kwargs):
        group_id = kwargs.get('pk')
        try:
            group = TripGroup.objects.get(id=group_id)
        except TripGroup.DoesNotExist:
            return Response({'error': 'Gruppo non trovato'}, status=status.HTTP_404_NOT_FOUND)

        group.members.add(request.user)
        return Response({'message': 'Unito al gruppo con successo'}, status=status.HTTP_200_OK)

class TripGroupPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        assert_user_is_group_member(self.request.user, group_id)  # verifica accesso
        return Post.objects.filter(group_id=group_id).order_by('-created_at')

class TripGroupDetailView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TripGroupSerializer

    def get(self, request, group_id):
        group = assert_user_is_group_member(request.user, group_id)
        serializer = self.get_serializer(group)
        return Response(serializer.data)
