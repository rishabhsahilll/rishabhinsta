# Generated by Django 5.0.1 on 2024-03-26 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='wing',
            field=models.CharField(blank=True, choices=[('ARMY', 'ARMY'), ('NAVY', 'NAVY'), ('AIR FORCE', 'AIR FORCE'), ('TECHNOLOGY', 'TECHNOLOGY')], max_length=10),
        ),
    ]
