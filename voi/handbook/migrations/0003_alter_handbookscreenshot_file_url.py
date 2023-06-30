# Generated by Django 4.2.1 on 2023-06-24 12:16

from django.db import migrations, models
import handbook.models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0002_alter_handbook_body_alter_handbook_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handbookscreenshot',
            name='file_url',
            field=models.FileField(upload_to=handbook.models.url_upload_to_for_handbook),
        ),
    ]
