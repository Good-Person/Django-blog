# coding=utf8

from django import template
from blog.models import *

register = template.Library()

@register.inclusion_tag('blog/left-column.html')
def get_left_column():
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return {
            'categories':categories,
            'tags':tags,
            }