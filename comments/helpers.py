from rest_framework.exceptions import PermissionDenied
from posts.models import Post

#funzione per verificare se si può commentare un post
def assert_user_can_comment_post(user, post_id):
    try:
        post = Post.objects.select_related('group').get(id=post_id)
    except Post.DoesNotExist:
        raise PermissionDenied("Post non trovato.")

    if user not in post.group.members.all():
        raise PermissionDenied("Non sei membro del gruppo di questo post.")

    return post
