# Generated by Django 5.2.1 on 2025-05-21 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('time', models.TimeField(auto_now_add=True, null=True)),
                ('order_id', models.CharField(max_length=50)),
                ('payment_id', models.CharField(max_length=50)),
                ('device_id', models.IntegerField()),
                ('ordered_vanilla', models.IntegerField(default=0)),
                ('ordered_chocolate', models.IntegerField(default=0)),
                ('ordered_strawberry', models.IntegerField(default=0)),
                ('delivered_vanilla', models.IntegerField(default=0)),
                ('delivered_chocolate', models.IntegerField(default=0)),
                ('delivered_strawberry', models.IntegerField(default=0)),
                ('is_payment_successful', models.BooleanField(default=False)),
                ('our_order_id', models.BigIntegerField()),
                ('is_all_items_delivered', models.BooleanField(default=False)),
            ],
        ),
    ]
