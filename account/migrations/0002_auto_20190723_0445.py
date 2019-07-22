# Generated by Django 2.2.3 on 2019-07-23 04:45

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, validators=[account.models.phone_number_validator]),
        ),
    ]
