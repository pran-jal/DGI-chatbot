# Generated by Django 4.0.3 on 2023-03-22 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='modified_at',
        ),
        migrations.RemoveField(
            model_name='response',
            name='modified_at',
        ),
    ]
