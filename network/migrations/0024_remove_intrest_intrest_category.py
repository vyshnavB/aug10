# Generated by Django 4.1.3 on 2023-07-31 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0023_intrest_category_alter_intrest_intrest_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intrest',
            name='intrest_category',
        ),
    ]
