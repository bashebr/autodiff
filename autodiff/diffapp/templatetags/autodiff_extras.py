import re 

from django import template
register = template.Library()  # register the template to 

# use decorators to register the filter
@register.filter(name='replace')
def replace ( string, args ): 
    search  = args.split(args[0])[1]
    replace = args.split(args[0])[2]

    return re.sub( search, replace, string )