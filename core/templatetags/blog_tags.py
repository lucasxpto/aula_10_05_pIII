from core.models import Post

from django import template

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.publicados.count()


@register.inclusion_tag("blog/post/ultimos.html")
def mostrar_ultimos_posts(count=5):
    posts = Post.publicados.order_by('-publicado')[:count]
    return {'ultimos': posts}
