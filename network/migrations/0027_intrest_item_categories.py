# Generated by Django 4.1.3 on 2023-07-31 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0026_item_categories_delete_intr_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='intrest',
            name='item_categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.item_categories'),
        ),
    ]