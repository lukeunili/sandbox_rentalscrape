# Generated by Django 3.0.10 on 2021-04-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0014_auto_20210401_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='dropoffdate',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='pickupdate',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]
