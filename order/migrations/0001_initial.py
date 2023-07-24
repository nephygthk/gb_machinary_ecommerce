# Generated by Django 4.2.3 on 2023-07-24 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_media_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=100)),
                ('Country', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('total_paid', models.DecimalField(decimal_places=2, max_digits=9)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=9)),
                ('order_key', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Delivery in Progress', 'Delivery in Progress'), ('Delivered', 'Delivered')], max_length=150)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='store.product')),
            ],
        ),
    ]
