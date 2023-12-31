# Generated by Django 4.2.3 on 2023-07-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending, awaiting payment', 'Pending, awaiting payment'), ('Delivery in Progress', 'Delivery in Progress'), ('Delivered', 'Delivered'), ('Stopped by custom', 'Stopped by custom')], default='Pending, awaiting payment', max_length=150),
        ),
    ]
