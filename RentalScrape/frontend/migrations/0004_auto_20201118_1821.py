# Generated by Django 3.1.2 on 2020-11-18 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20201105_1537'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Offer',
            new_name='OfferList',
        ),
    ]