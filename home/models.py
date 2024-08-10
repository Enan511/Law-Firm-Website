from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='home/static/media')
    date_published = models.DateField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
