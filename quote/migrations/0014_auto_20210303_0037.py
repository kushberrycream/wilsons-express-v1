# Generated by Django 3.1.4 on 2021-03-03 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0013_auto_20210303_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='c_date',
            field=models.DateField(blank=True, default='2012-09-04'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='d_date',
            field=models.DateField(blank=True, default='2012-09-04'),
        ),
    ]
