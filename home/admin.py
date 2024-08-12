from django.contrib import admin
from .models import News


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'date_published', 'author', 'created_at', 'updated_at')
