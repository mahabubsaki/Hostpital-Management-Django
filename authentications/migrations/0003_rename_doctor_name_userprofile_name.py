# Generated by Django 4.1.10 on 2023-09-08 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0002_rename_name_userprofile_doctor_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='doctor_name',
            new_name='name',
        ),
    ]
