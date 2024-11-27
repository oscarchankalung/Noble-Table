from django import template

register = template.Library()

@register.filter
def to_dollar(value:str):
    return f"${value}"

@register.filter
def to_upper(value:str):
    return value.upper()

@register.filter
def to_lower(value:str):
    return value.lower()