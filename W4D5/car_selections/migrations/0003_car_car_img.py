# Generated by Django 4.1.5 on 2023-01-29 01:52

import ckeditor.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('car_selections', '0002_alter_car_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_img',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]