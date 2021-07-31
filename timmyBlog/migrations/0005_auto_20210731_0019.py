# Generated by Django 3.2.5 on 2021-07-31 00:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timmyBlog', '0004_postimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostImage',
        ),
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]