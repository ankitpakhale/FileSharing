# Generated by Django 3.2.11 on 2022-01-24 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filelist',
            old_name='recieved_from2',
            new_name='recieved_from',
        ),
        migrations.RemoveField(
            model_name='userdetails2',
            name='userfiles',
        ),
        migrations.AddField(
            model_name='userdetails2',
            name='userfiles',
            field=models.ManyToManyField(to='share2.FileList'),
        ),
    ]
