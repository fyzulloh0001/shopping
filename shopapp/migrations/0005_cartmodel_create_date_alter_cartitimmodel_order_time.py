# Generated by Django 4.0.1 on 2022-08-04 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_alter_cartmodel_cart_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmodel',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cartitimmodel',
            name='order_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
