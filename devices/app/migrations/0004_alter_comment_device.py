# Generated by Django 4.2.6 on 2023-11-10 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_comment_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.device'),
        ),
    ]