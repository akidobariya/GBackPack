# Generated by Django 5.0.2 on 2024-03-05 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_rename_name_register_data_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_data',
            name='mobilenumber',
            field=models.IntegerField(),
        ),
    ]
