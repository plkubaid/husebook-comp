# Generated by Django 2.0 on 2018-02-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0011_auto_20180222_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tranrecord',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
