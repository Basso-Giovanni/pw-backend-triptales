from django.contrib.auth import get_user_model, authenticate
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from trips.models import TripGroup
from trips.serializers import TripGroupSerializer
from .serializers import UserSerializer

# View per ottenere il profilo utente
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user  # L'utente autenticato tramite il token
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# View per aggiornare il profilo utente
class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        user = request.user  # Ottieni l'utente autenticato

        # Usa il serializer per validare i dati e aggiornare l'utente
        serializer = UserSerializer(user, data=request.data, partial=True)  # 'partial=True' consente di aggiornare solo i campi forniti

        if serializer.is_valid():
            serializer.save()  # Salva i cambiamenti nel database
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View per la registrazione di un nuovo utente
class RegisterUserView(APIView):
    def post(self, request, *args, **kwargs):
        # Ottieni il modello utente personalizzato
        CustomUser = get_user_model()

        # Verifica se l'username esiste già
        username = request.data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            return Response({"error": "Questo username è già stato preso."}, status=status.HTTP_400_BAD_REQUEST)

        # Verifica se l'email è già registrata
        email = request.data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            return Response({"error": "Questa email è già registrata."}, status=status.HTTP_400_BAD_REQUEST)

        # Procedi con la creazione dell'utente se l'username e l'email sono validi
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Crea l'utente nel database
            token = Token.objects.create(user=user)  # Crea il token per l'utente
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View per il login dell'utente
class LoginUserView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # Autenticazione dell'utente
        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class MyTripGroupsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        group_ids = TripGroup.objects.filter(members=user).values_list('id', flat=True)
        return Response(list(group_ids))
