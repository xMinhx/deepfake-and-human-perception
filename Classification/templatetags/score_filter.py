from django import template

register = template.Library()

#Calculates the performance in percentage, adds a new custom tags for django tags
@register.filter
def percentage( value, arg ):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = int( value )
        arg = int( arg )
        if arg: return int(value / arg*100)
    except: pass
    return ''
