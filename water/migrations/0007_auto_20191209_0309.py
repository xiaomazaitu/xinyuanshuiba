# Generated by Django 2.0.4 on 2019-12-09 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0006_auto_20191206_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name='orderaddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='orderphone',
            field=models.CharField(max_length=20, null=True, verbose_name='orderphone'),
        ),
    ]
