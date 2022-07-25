# Generated by Django 4.0.1 on 2022-07-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0004_alter_usermodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='UserModel_Image'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
