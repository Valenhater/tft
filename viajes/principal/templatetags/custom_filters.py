from django import template

register = template.Library()

@register.filter
def index(List, i):
    return List[i]

@register.filter
def multiply(a, b):
    return a * b