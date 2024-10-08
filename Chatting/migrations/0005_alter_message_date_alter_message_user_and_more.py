# Generated by Django 5.0.7 on 2024-08-06 03:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatting', '0004_alter_message_date_alter_message_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=10000),
        ),
    ]
