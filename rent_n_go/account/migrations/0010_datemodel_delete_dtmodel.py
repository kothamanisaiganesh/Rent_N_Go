# Generated by Django 4.1 on 2023-01-27 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_dtmodel_delete_bookingdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_car', models.BooleanField(default=False, verbose_name='Car')),
                ('is_bike', models.BooleanField(default=False, verbose_name='Bike')),
                ('name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='DTModel',
        ),
    ]
