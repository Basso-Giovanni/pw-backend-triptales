from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostSerializer
from .badge_utils import check_and_assign_user_badge
from .helpers import assert_user_is_group_member
from .models import TripGroup, UserGroupBadge
from .serializers import TripGroupSerializer, BadgeSerializer


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
        # Assegna o aggiorna il badge per l'utente nel gruppo
        check_and_assign_user_badge(request.user, group)

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

class UserGroupBadgeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, group_id):
        # Verifica che l'utente sia membro del gruppo
        group = assert_user_is_group_member(request.user, group_id)

        try:
            user_badge = UserGroupBadge.objects.get(user=request.user, group=group)
            badge_data = BadgeSerializer(user_badge.badge).data
        except UserGroupBadge.DoesNotExist:
            badge_data = None

        return Response({'badge': badge_data})
