# Generated by Django 4.2.3 on 2023-07-22 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
