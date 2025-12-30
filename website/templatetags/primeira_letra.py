from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter

def primeira_letra(value):
    try:
        return value[0]
    except Exception:
        return ''