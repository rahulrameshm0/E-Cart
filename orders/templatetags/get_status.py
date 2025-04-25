from django import template
register = template.Library()

@register.simple_tag(name='get_status')
def get_total(status):
    status = status-1
    status_arry = ['confirmed','processed','deliverd','rejected']
    return status_arry[status]
