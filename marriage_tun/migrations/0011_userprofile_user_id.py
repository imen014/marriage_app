# Generated by Django 5.1.2 on 2024-10-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marriage_tun', '0010_remove_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]