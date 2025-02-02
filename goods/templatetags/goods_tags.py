from goods.models import categories
from django import template

register = template.Library()

@register.simple_tag()
def tag_categories():
    return categories.objects.all()