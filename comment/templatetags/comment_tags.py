# coding=utf8

from django import template



register = template.Library()

@register.inclusion_tag('comment/comment.html')
def get_comments(article):
    comments = article.get_comments()
    return {
            "comments":comments,
            "article":article,
            }