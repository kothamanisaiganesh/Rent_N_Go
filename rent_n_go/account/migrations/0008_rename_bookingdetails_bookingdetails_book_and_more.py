# Generated by Django 4.1 on 2023-01-23 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_rename_date1_bookingdetails_date1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingdetails',
            old_name='bookingdetails',
            new_name='book',
        ),
        migrations.RemoveField(
            model_name='bookingdetails',
            name='date1',
        ),
        migrations.RemoveField(
            model_name='bookingdetails',
            name='date2',
        ),
        migrations.RemoveField(
            model_name='bookingdetails',
            name='location',
        ),
        migrations.RemoveField(
            model_name='bookingdetails',
            name='time1',
        ),
        migrations.RemoveField(
            model_name='bookingdetails',
            name='time2',
        ),
    ]
