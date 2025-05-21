from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import UserProfileView, UpdateProfileView, RegisterUserView, LoginUserView, MyTripGroupsView, \
    UserProfileViewByID

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'), #registrazione dell'utente
    path('login/', LoginUserView.as_view(), name='login'), #login dell'utente
    path('profile/', UserProfileView.as_view(), name='user-profile'), #login dell'utente (per ottenere i dati)
    path('profile/<int:user_id>/', UserProfileViewByID.as_view(), name='user-profile-by-id'), #profilo pubblico dell'utente
    path('profile/update/', UpdateProfileView.as_view(), name='update-profile'), #per aggiornare il profilo dell'utente
    path('my-trips/', MyTripGroupsView.as_view(), name='my-trip-group'), #per vedere i gruppi a cui è iscritto l'utente
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #per la foto profilo
