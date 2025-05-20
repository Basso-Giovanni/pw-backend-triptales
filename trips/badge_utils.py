from .models import Badge, UserGroupBadge
from posts.models import Post
from comments.models import Comment
from django.db.models import Count, Q

def assign_unique_badge(user, group, badge_name, description=""):
    badge, _ = Badge.objects.get_or_create(name=badge_name, defaults={"description": description})
    UserGroupBadge.objects.update_or_create(
        user=user,
        group=group,
        defaults={"badge": badge}
    )

def evaluate_badge(user, group):
    # Conteggio post creati dall'utente nel gruppo
    post_count = Post.objects.filter(created_by=user, group=group).count()

    # Conteggio commenti scritti dall'utente nei post del gruppo
    comment_count = Comment.objects.filter(author=user, post__group=group).count()

    # Conteggio totale like ricevuti dall'utente nei suoi post nel gruppo
    likes_received = Post.objects.filter(created_by=user, group=group).annotate(num_likes=Count('likes')).aggregate(total_likes=Count('likes'))['total_likes'] or 0

    # Conteggio totale like dati dall'utente nei post del gruppo
    # Poiché likes è ManyToManyField in Post, dobbiamo contare quanti post dell gruppo ha likato l'utente
    likes_given = Post.objects.filter(group=group, likes=user).count()

    # Ora assegniamo badge in base a queste metriche
    if post_count >= 10:
        return "Fotografo", "Ha pubblicato almeno 10 post nel gruppo."
    if comment_count >= 10:
        return "Sociale", "Ha scritto almeno 10 commenti nel gruppo."
    if likes_received >= 20:
        return "Popolare", "Ha ricevuto almeno 20 like nel gruppo."
    if likes_given >= 50:
        return "Fanatic Like", "Ha messo almeno 50 like nel gruppo."

    return "Partecipante", "Membro attivo del gruppo."

def check_and_assign_user_badge(user, group):
    badge_name, description = evaluate_badge(user, group)
    assign_unique_badge(user, group, badge_name, description)
