# Generated by Django 4.1.3 on 2023-07-20 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0017_uploadedfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content_image',
        ),
        migrations.AddField(
            model_name='post',
            name='content_images',
            field=models.ManyToManyField(blank=True, to='network.uploadedfile'),
        ),
    ]