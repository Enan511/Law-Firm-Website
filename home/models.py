from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os


class News(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='news')
    date_published = models.DateField()
    author = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Checking if the instance already exists in the database
            self.updated_at = timezone.now()
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


@receiver(pre_delete, sender=News)
def delete_news_image(sender, instance, **kwargs):
    # Delete the associated image file
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
