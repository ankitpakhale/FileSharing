# Generated by Django 3.2.11 on 2022-01-27 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share2', '0005_auto_20220127_0717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ip',
            old_name='global_ipaddress',
            new_name='ipaddress',
        ),
        migrations.RemoveField(
            model_name='ip',
            name='local_ipaddress',
        ),
    ]