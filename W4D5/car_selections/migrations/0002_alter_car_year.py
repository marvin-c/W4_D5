# Generated by Django 4.1.5 on 2023-01-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_selections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(max_length=4),
        ),
    ]