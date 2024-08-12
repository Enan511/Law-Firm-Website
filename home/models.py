from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class News(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='news')
    date_published = models.DateField()
    author = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)


class Comment(models.Model):
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
