# Generated by Django 4.2.6 on 2023-11-10 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_device_sticker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='wtf',
        ),
    ]
