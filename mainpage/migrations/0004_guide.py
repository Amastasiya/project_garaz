# Generated by Django 4.1.4 on 2022-12-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_remove_employee_date_of_birth_employee_birthdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(default='', max_length=1024)),
                ('surname', models.CharField(default='', max_length=1024)),
                ('name', models.CharField(default='', max_length=1024)),
                ('fathername', models.CharField(default='', max_length=1024)),
                ('birth_date', models.DateField()),
                ('phone_working', models.IntegerField()),
                ('phone_personal', models.IntegerField()),
                ('email_working', models.CharField(default='', max_length=1024)),
            ],
        ),
    ]