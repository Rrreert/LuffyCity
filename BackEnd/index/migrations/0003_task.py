# Generated by Django 2.2.5 on 2020-04-06 11:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RBAC', '0005_role_duty'),
        ('index', '0002_project_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapters', models.CharField(max_length=64, verbose_name='模块章节')),
                ('title', models.CharField(max_length=32, verbose_name='题目')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交时间')),
                ('achievement', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='成绩')),
                ('comment', models.TextField(verbose_name='老师点评')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='index.Student', verbose_name='学生')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='RBAC.RbacUserInfo', verbose_name='批改老师')),
            ],
        ),
    ]