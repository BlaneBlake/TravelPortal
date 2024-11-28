# Generated by Django 5.0.6 on 2024-11-27 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Blog', '0004_remove_post_main_image_delete_postimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='Blog.post')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_photos/')),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='Gallery.gallery')),
            ],
        ),
    ]