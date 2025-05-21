from django.contrib.auth import get_user_model, authenticate
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from trips.models import TripGroup
from .serializers import UserSerializer

CustomUser = get_user_model()

#view per ottenere profilo utente
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user  #l'utente deve essere autenticato
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

#view per vedere il profilo pubblico
class UserProfileViewByID(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id, *args, **kwargs):
        user = get_object_or_404(CustomUser, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

#view per aggiornare il profilo
class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#view per registrare un nuovo utente
class RegisterUserView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username') #controlla se c'è già lo stesso username
        if CustomUser.objects.filter(username=username).exists():
            return Response({"error": "Questo username è già stato preso."}, status=status.HTTP_400_BAD_REQUEST)

        email = request.data.get('email') #controlla se c'è già la stessa email
        if CustomUser.objects.filter(email=email).exists():
            return Response({"error": "Questa email è già registrata."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)  #crea il token per l'utente
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#view per il login dell'utente
class LoginUserView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password) #autenticazione

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

#view per ottenere la lista dei gruppi
class MyTripGroupsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        group_ids = TripGroup.objects.filter(members=user).values_list('id', flat=True)
        return Response(list(group_ids))
