# Generated by Django 4.2.1 on 2023-05-31 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_rename_avatar_user_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageprofile',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
