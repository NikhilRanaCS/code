# Generated by Django 4.2 on 2024-03-03 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_userdata_order_id_remove_userdata_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='dropdown_list',
            new_name='option_selected',
        ),
    ]