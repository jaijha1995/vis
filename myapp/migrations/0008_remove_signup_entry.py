# Generated by Django 4.1.1 on 2022-09-30 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_signup_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='entry',
        ),
    ]