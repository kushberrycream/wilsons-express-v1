# Generated by Django 3.1.4 on 2021-03-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0018_quote_spec_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='spec_service',
            field=models.CharField(max_length=20),
        ),
    ]
