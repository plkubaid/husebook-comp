# Generated by Django 2.0 on 2018-03-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_open_support'),
    ]

    operations = [
        migrations.AddField(
            model_name='open_support',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default='2018-02-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='support',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default='2018-02-01'),
            preserve_default=False,
        ),
    ]
