# Generated by Django 5.0.8 on 2024-08-11 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_news_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='home.news')),
            ],
        ),
    ]
