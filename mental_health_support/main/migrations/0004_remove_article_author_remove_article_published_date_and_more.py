# Generated by Django 5.0.7 on 2024-07-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_journal_news_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='published_date',
        ),
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='journal',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
