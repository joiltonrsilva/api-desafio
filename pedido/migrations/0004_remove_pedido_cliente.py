# Generated by Django 5.1.3 on 2024-11-09 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_pedido_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='cliente',
        ),
    ]
