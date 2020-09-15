from django import template
register=template.Library()
def capitalise(value):
    return value.capitalize()
    
register.filter('capitalise',capitalise)


