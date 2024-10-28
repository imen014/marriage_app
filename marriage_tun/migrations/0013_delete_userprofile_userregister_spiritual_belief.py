# Generated by Django 5.1.2 on 2024-10-26 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marriage_tun', '0012_remove_userprofile_values'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='userregister',
            name='spiritual_belief',
            field=models.CharField(blank=True, choices=[('Agnostic', 'Agnostic'), ('Atheist', 'Atheist'), ('Christian', 'Christian'), ('Muslim', 'Muslim'), ('Hindu', 'Hindu'), ('Buddhist', 'Buddhist'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]