# Generated by Django 3.1.4 on 2021-10-11 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hospital', '0002_delete_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospital_name', models.CharField(max_length=50)),
                ('Doctor_name', models.CharField(max_length=50)),
                ('Clinic', models.CharField(max_length=50)),
            ],
        ),
    ]
