# Generated by Django 3.0.10 on 2021-04-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_offer_searchid'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='imgurl',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='pickupstationid',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='returnstationid',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='bookingclass',
            field=models.CharField(blank=True, default='', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='cardescription',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='cartype',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='dropoffdate',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='mileage',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='pickupdate',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='price',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='searchid',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]