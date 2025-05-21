from rest_framework.exceptions import PermissionDenied
from .models import TripGroup

#funzione per verificare se l'utente è iscritto al gruppo
def assert_user_is_group_member(user, group_id):
    try:
        group = TripGroup.objects.get(id=group_id)
    except TripGroup.DoesNotExist:
        raise PermissionDenied("Gruppo non trovato.")

    if user not in group.members.all():
        raise PermissionDenied("Non sei membro di questo gruppo.")

    return group
