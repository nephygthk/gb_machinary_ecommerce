# Generated by Django 4.2.3 on 2023-07-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivery in Progress', 'Delivery in Progress'), ('Delivered', 'Delivered'), ('Stopped by custom', 'Stopped by custom')], max_length=150),
        ),
    ]
