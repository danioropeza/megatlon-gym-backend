# Generated by Django 2.2 on 2019-05-18 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20190512_2350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='mail',
            new_name='email',
        ),
    ]