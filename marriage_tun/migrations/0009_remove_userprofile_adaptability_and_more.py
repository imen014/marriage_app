# Generated by Django 5.1.2 on 2024-10-26 18:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marriage_tun', '0008_alter_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='adaptability',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='career_ambition',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='communication_style',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='confidence',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='conflict_management',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='emotional_maturity',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='empathy',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='financial_management',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='future_goals',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='hobbies',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='humor_sense',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='kindness',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='lifestyle',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='listening_skills',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='openness',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='physical_activity_level',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='preferred_appearance',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='resilience',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
