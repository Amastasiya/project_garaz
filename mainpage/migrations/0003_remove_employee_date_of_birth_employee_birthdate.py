# Generated by Django 4.1.4 on 2022-12-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_rename_email_employee_email_working_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='employee',
            name='birthdate',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]