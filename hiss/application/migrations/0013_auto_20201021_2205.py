# Generated by Django 2.2.13 on 2020-10-22 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_merge_20201021_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='question2',
            field=models.TextField(max_length=500, verbose_name='This is a question?'),
        ),
    ]
