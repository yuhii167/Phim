# Generated by Django 4.1.7 on 2023-03-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phim', '0019_remove_category_approved_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='category',
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ManyToManyField(related_name='movies', to='phim.category'),
        ),
    ]
