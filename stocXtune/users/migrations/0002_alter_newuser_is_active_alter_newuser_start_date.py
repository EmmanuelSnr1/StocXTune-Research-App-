# Generated by Django 4.0.3 on 2022-04-26 07:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
