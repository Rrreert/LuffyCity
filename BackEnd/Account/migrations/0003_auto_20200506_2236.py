# Generated by Django 3.0.3 on 2020-05-06 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20200506_1611'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
