# Generated by Django 4.2.1 on 2023-06-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handbook',
            name='body',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='handbook',
            name='title',
            field=models.TextField(max_length=100),
        ),
    ]
