# Generated by Django 5.0.7 on 2024-07-21 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='journal_images/'),
        ),
    ]
