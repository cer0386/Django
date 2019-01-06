# Generated by Django 2.1.4 on 2019-01-06 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hobbies', '0005_auto_20181217_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserv_form',
            fields=[
                ('reservationID_temp', models.IntegerField(primary_key=True, serialize=False)),
                ('pickupD', models.DateField(verbose_name='Pickup date')),
                ('returnD', models.DateField(verbose_name='Return date')),
                ('cars', models.ManyToManyField(to='hobbies.Car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hobbies.Customer')),
            ],
        ),
    ]