from rest_framework import generics, permissions
from .models import Image
from .serializers import ImageSerializer

#view per caricare l'immagine
class CreateImageView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

#view per vedere l'immagine
class ImageDetailView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]
