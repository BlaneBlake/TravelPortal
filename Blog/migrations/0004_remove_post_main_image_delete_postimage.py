# Generated by Django 5.0.6 on 2024-11-27 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_post_latitude_post_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='main_image',
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]