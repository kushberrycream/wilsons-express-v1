# Generated by Django 3.1.4 on 2021-03-08 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0032_auto_20210306_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, help_text="Max 30kg's", max_digits=5)),
                ('height', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('length', models.PositiveIntegerField()),
                ('volume_weight', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='quote.quote')),
            ],
        ),
    ]
