# Generated by Django 2.0 on 2018-02-16 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='price_per_unit',
            new_name='price',
        ),
    ]
