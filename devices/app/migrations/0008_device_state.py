# Generated by Django 4.2.6 on 2023-11-10 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_device_wtf'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='state',
            field=models.CharField(blank=True, choices=[('И', 'Используется'), ('З', 'В запасе'), ('С', 'Вышел из строя')], max_length=1, null=True),
        ),
    ]
