from django import template

register=template.Library()

@register.filter
def strtolist(string): 
    return list(string.split(","))

@register.filter(name='zip')
def zip_lists(a, b):
  return zip(a, b)

@register.filter()
def to_int(value):
    return int(value)
