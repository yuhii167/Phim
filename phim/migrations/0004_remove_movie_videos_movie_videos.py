# Generated by Django 4.1.7 on 2023-03-09 10:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phim', '0003_video_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='videos',
        ),
        migrations.AddField(
            model_name='movie',
            name='videos',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='Video'),
            preserve_default=False,
        ),
    ]
