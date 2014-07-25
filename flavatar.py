from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from hashlib import md5

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def flavatar(value):
    fistchar = value[:1].upper()
    value = value.encode('utf-8')
    hash = md5(value).hexdigest()
    hash_values = (hash[:8], hash[8:16], hash[16:24])
    number = tuple(int(value, 16)%256 for value in hash_values)

    return mark_safe('<div class="media-object flavatar" style="background: rgb%s;">%s</div>' % (number, fistchar))
