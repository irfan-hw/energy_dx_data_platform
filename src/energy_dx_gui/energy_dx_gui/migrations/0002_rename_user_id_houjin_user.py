# Generated by Django 3.2.18 on 2023-04-21 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('energy_dx_gui', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='houjin',
            old_name='user_id',
            new_name='user',
        ),
    ]