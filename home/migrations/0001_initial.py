# Generated by Django 5.0.8 on 2024-08-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='news_images/')),
                ('date_published', models.DateField()),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]