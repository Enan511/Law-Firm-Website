# Generated by Django 5.0.8 on 2024-08-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content_file',
            field=models.FileField(blank=True, null=True, upload_to='news_files'),
        ),
    ]