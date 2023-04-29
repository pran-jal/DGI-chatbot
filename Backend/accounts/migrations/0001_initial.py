# Generated by Django 4.0.3 on 2023-03-22 18:11

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.IntegerField(editable=False, unique=True, validators=[accounts.models.validate_mobile_no])),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
    ]
