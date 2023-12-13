# Generated by Django 4.2.6 on 2023-11-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_device_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='device',
            name='state',
            field=models.CharField(blank=True, choices=[('И', 'Используется'), ('У', 'Установлен'), ('Д', 'Демонтирован'), ('З', 'В запасе'), ('С', 'Вышел из строя')], default=('З', 'В запасе'), max_length=1, null=True),
        ),
    ]
