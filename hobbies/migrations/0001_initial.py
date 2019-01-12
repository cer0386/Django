# Generated by Django 2.1.4 on 2019-01-12 15:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('spz', models.CharField(max_length=7, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(7)])),
                ('bought', models.DateField(verbose_name='Car was bought')),
                ('stk', models.DateField(verbose_name='STK expiracy')),
                ('nOAccidents', models.IntegerField()),
                ('pricePerDay', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('driverLicense', models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(8)])),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('houseNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('joined', models.DateField(verbose_name='Joined company')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservationNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('customer', models.CharField(max_length=150)),
                ('employee', models.CharField(max_length=150)),
                ('pickupD', models.DateField(null=True, verbose_name='Pickup date')),
                ('returnD', models.DateField(null=True, verbose_name='Return date')),
                ('cars', models.ManyToManyField(to='hobbies.Car')),
            ],
        ),
        migrations.CreateModel(
            name='ReservForm',
            fields=[
                ('reservationID_temp', models.IntegerField(primary_key=True, serialize=False)),
                ('customer', models.CharField(max_length=150)),
                ('cars', models.CharField(max_length=150)),
                ('pickupD', models.DateField(verbose_name='Pickup date')),
                ('returnD', models.DateField(verbose_name='Return date')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hobbies.Position'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hobbies.Model'),
        ),
    ]
