# Generated by Django 4.1.4 on 2022-12-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(default='', max_length=1024)),
                ('surname', models.CharField(default='', max_length=1024)),
                ('name', models.CharField(default='', max_length=1024)),
                ('fathername', models.CharField(default='', max_length=1024)),
                ('date_of_birth', models.DateTimeField()),
                ('phone', models.IntegerField()),
                ('email', models.CharField(default='', max_length=1024)),
            ],
        ),
    ]