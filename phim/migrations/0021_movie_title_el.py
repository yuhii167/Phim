# Generated by Django 4.1.7 on 2023-03-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phim', '0020_remove_movie_category_movie_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='title_el',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
