# Generated by Django 3.0.7 on 2020-06-25 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0002_auto_20200623_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author_name',
        ),
    ]
