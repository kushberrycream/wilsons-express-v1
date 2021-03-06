# Generated by Django 3.1.4 on 2021-02-18 23:12

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('create_account', '0006_auto_20210218_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Done_accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(blank=True, max_length=80)),
                ('town_or_city', models.CharField(max_length=40)),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('freight', models.CharField(choices=[('mechanical', 'Mechanical'), ('plants_botanical', 'Plants and Botanical'), ('live_fish', 'Live Fish'), ('perishable', 'Perishable Items'), ('alcohol', 'Alcohol'), ('Other', 'Other Please Specify')], max_length=250)),
                ('other_comments', models.TextField(blank=True)),
                ('complete', models.BooleanField(default=False, help_text='Only Select Complete Once Account is 100% Set Up!', verbose_name='Complete')),
            ],
            options={
                'verbose_name': 'Done',
                'verbose_name_plural': 'Done',
            },
        ),
    ]
