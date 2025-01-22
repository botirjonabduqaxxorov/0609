from django import template
from flowers.models import Type

register = template.Library()

@register.simple_tag
def get_all_types():
    return Type.objects.all()
