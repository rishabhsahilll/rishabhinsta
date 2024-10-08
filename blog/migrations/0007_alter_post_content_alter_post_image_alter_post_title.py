# Generated by Django 5.0.1 on 2024-09-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_post_video_alter_postreport_reason_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="post_images"),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
