# Generated by Django 2.2.6 on 2019-11-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogauthor',
            name='stug',
            field=models.SlugField(default=True, max_length=40),
            preserve_default=False,
        ),
    ]
