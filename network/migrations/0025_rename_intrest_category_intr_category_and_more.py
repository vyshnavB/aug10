# Generated by Django 4.1.3 on 2023-07-31 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0024_remove_intrest_intrest_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='intrest_category',
            new_name='intr_category',
        ),
        migrations.RenameField(
            model_name='intr_category',
            old_name='intrest_category',
            new_name='intr_category',
        ),
    ]
