# Generated by Django 5.0.6 on 2024-12-01 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0003_photo_is_main'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='title',
            new_name='gallery_title',
        ),
    ]
