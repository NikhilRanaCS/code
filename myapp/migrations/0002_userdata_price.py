# Generated by Django 4.2 on 2024-03-01 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='price',
            field=models.IntegerField(default=449),
        ),
    ]