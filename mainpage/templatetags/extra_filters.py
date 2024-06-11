# your_app/templatetags/extra_filters.py
from django import template

register = template.Library()

@register.filter(name='dict_get')
def dict_get(dictionary, key):
    if dictionary and key in dictionary:
        return dictionary[key]
    else:
        return None  # or any default value you prefer
