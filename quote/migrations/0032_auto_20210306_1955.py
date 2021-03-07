# Generated by Django 3.1.4 on 2021-03-06 19:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0031_auto_20210306_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='fragile',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='security',
        ),
        migrations.AddField(
            model_name='quote',
            name='actual_weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='quote',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='quote_ref',
            field=models.CharField(default=django.utils.timezone.now, editable=False, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='volume_weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
