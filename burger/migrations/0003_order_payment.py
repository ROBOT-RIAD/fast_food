# Generated by Django 5.0.2 on 2024-08-23 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger', '0002_rename_coustomer_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
