# Generated by Django 3.1.4 on 2021-03-01 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0009_auto_20210301_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='d_postcode',
            field=models.CharField(max_length=8, verbose_name='Delivery Postcode'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='weight',
            field=models.PositiveIntegerField(help_text='KGs'),
        ),
    ]
