from datetime import datetime

from django.db import models
from users.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField('Заголовок')
    link = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, null=True)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField('Текст')
    date = models.DateTimeField(default=datetime.now, null=True)


class Upvote(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
