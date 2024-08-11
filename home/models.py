from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content_file = models.FileField(upload_to='news_files',blank=True,null=True)
    image = models.ImageField(upload_to='news')
    date_published = models.DateField()
    author = models.CharField(max_length=100)

    @property
    def content(self):
        if self.content_file:
            return self.content_file.read().decode('utf-8')
        return ""
