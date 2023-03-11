from django import template
from ..models import Menu

register = template.Library()

@register.filter(name='has_vote')
def has_vote(user, pk):
    menu = Menu.objects.get(pk = pk)
    for attender in menu.Vistors_list.all():
        if attender==user:
            return True
    