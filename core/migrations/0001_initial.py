# Generated by Django 4.1.10 on 2023-09-08 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentications', '0006_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('issue', models.CharField(choices=[('', 'Select Issue'), ('Nephrologist Patient', 'Nephrologist Patient'), ('Pediatrician Patient', 'Pediatrician Patient'), ('Eye Patient', 'Eye Patient'), ('Parental Patient', 'Parental Patient'), ('Liver Patient', 'Liver'), ('Heart Patient', 'Heart Patient')], max_length=30)),
                ('appointment_date', models.DateTimeField()),
                ('doctor', models.ManyToManyField(to='authentications.userprofile')),
            ],
        ),
    ]
