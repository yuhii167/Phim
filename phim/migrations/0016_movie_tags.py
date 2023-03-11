# Generated by Django 4.1.7 on 2023-03-11 13:20

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('phim', '0015_ads'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]