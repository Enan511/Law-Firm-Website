# Generated by Django 5.0.8 on 2024-08-11 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_news_content_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
    ]
