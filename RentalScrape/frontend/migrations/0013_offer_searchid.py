# Generated by Django 3.0.10 on 2020-11-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_auto_20201123_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='searchid',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
