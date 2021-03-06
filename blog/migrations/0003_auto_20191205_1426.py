# Generated by Django 2.2.6 on 2019-12-05 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_blogauthor_stug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogauthor',
            name='stug',
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(help_text='Enter your blog text here.', max_length=400),
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Enter your comment here', max_length=400)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Blog')),
            ],
        ),
    ]
