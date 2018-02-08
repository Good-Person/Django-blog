# coding=utf8
from django.conf import settings
from django.core.mail import send_mail
from comment.models import Comment

def send_to_me(article):

    email_title = u'有新评论'
    url = 'http://huigege.xin/blog/article/%d' % article.id
    email_content = u'{}的文章下有新的评论<a href="{}">查看博客</a>'.format(article.title, url)
    send_mail(email_title, '', settings.EMAIL_FROM, ["775470092@qq.com", ], fail_silently=True,
              html_message=email_content)


def send_to_reply(reply, article, user):
    send = []
    if reply.user:
        send.append(reply.user.email)
    comments = Comment.objects.filter(parent_reply=reply).all()
    for comment in comments:
        if comment.user:
            send.append(comment.user.email)
    send = list(set(send))
    if user:
        if user.email in send:
            send.remove(user.email)
    if not send:
        return
    email_title = u'有人回复你啦'
    url = 'http://huigege.xin/blog/article/%d' % article.id
    email_content = u'你在辉哥哥博客的评论有新的回复：<br>{}文章下的<br><a href="{}">点击查看详情</a>'.format(article.title, url)
    send_mail(email_title, '', settings.EMAIL_FROM, send, fail_silently=True,
              html_message=email_content)
