# Generated by Django 3.1.2 on 2020-11-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_auto_20201119_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='bookingclass',
            field=models.CharField(default=1234, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='mileage',
            field=models.CharField(default=700, max_length=50),
            preserve_default=False,
        ),
    ]
