from django import template

register = template.Library()

@register.filter
def index(List, i):
    return List[i]

@register.filter
def multiply(a, b):
    return a * b

@register.filter
def range_filter(value):
    return range(value)

@register.filter
def slice_list(value, arg):
    start, end = map(int, arg.split(':'))
    return value[start:end]
