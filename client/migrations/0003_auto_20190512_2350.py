# Generated by Django 2.2 on 2019-05-13 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20190512_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='cellphone',
            new_name='phoneNumber',
        ),
    ]
