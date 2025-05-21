from rest_framework.exceptions import PermissionDenied
from .models import TripGroup

#funzione per controllare se un utente è iscritto a un gruppo
def assert_user_is_group_member(user, group_id):
    try:
        group = TripGroup.objects.get(id=group_id)
    except TripGroup.DoesNotExist:
        raise PermissionDenied("Gruppo non trovato.")

    if user not in group.members.all():
        raise PermissionDenied("Non sei membro di questo gruppo.")

    return group