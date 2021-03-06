# Generated by Django 3.1.4 on 2021-03-01 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0008_auto_20210228_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='weight',
            field=models.PositiveIntegerField(default='1', help_text='KGs'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='c_company',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='quote',
            name='d_company',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
