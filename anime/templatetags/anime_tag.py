from django import template
from anime.models import Category, Anime

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('anime/tags/last_anime.html')
def get_last_anime(count=1):
    anime = Anime.objects.order_by('id')[:count]
    return {'last_anime': anime}
