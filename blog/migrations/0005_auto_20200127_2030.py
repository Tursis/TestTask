# Generated by Django 3.0.2 on 2020-01-27 20:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191209_1315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcomment',
            options={},
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
