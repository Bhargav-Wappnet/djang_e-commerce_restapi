# Generated by Django 4.2 on 2023-05-15 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_remove_order_items_order_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
