from django import template

# this is one way of registering filters
# register = template.Library()

# def cut(value, arg):
#     """
#         This cuts out all the values of "arg" from the string!
#     """
#     return value.replace(arg, '')

# # And now we need to register this filter as well. so vo bhi yhin hoga. 

# register.filter('cut', cut) # phly argument me ap filter ka naam pass kro gy , 2nd me wo function jis me wo filter bna va hai. 
 
# # Now this is another way of regsitering filter. YOu can either do it from above method or from below method.

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
        This cuts out all the values of "arg" from the string!
    """
    return value.replace(arg, '')










