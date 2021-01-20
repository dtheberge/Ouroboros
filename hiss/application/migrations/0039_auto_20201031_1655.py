# Generated by Django 2.2.13 on 2020-10-31 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0038_auto_20201031_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='shipping_address',
            field=models.BooleanField(choices=[(True, 'Agree'), (False, 'Disagree')], default=None, help_text='Note: US residents only and must be participating in Hacklahoma', verbose_name='Would you like to have swag shipped directly to you?'),
        ),
    ]
