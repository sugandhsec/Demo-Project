from django import template

register = template.Library()

@register.filter
def multiply(value):
    return value * 1.75


@register.filter
def titlecase(value):
    return value.title()
@register.filter
def paise(value):
    return int(value)*100

