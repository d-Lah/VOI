# Generated by Django 4.2.1 on 2023-06-01 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_imageprofile_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='reset_password_number',
            new_name='reset_password_uuid',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_activation_number',
            new_name='user_activation_uuid',
        ),
        migrations.RemoveField(
            model_name='imageprofile',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_avatar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('date_of_birth', models.DateTimeField()),
                ('user_avatar', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.imageprofile')),
            ],
        ),
        migrations.AddField(
            model_name='imageprofile',
            name='user_profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
            preserve_default=False,
        ),
    ]
