# Generated by Django 3.0.3 on 2020-05-15 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_auto_20200514_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='identity',
            field=models.IntegerField(choices=[(0, '管理员'), (2, '导师'), (3, '学员')], default=3, verbose_name='身份'),
        ),
    ]
