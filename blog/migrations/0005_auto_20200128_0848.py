# Generated by Django 3.0.1 on 2020-01-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191209_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
