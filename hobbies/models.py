from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
import datetime
from django import forms

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    joined = models.DateField('Joined company')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.surname + ' - ' + self.position.name

class Customer(models.Model):
    driverLicense = models.CharField(max_length=8, validators=[MinLengthValidator(8)], primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    houseNumber = models.IntegerField()


    def __str__(self):
        return self.name + ' ' + self.surname + ' --- ' + self.driverLicense

class Model(models.Model):
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.brand + ' ' + self.type

class Car(models.Model):

    spz = models.CharField(max_length=7, validators=[MinLengthValidator(7)], primary_key=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    bought = models.DateField('Car was bought')
    stk = models.DateField('STK expiracy')
    nOAccidents = models.IntegerField()
    pricePerDay = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return (('%s : ' + self.model.type + ' ' + self.model.brand + ' --- %s') % (self.spz, self.nOAccidents))




class Reservation(models.Model):
    reservationNumber = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    cars = models.ManyToManyField(Car)
    pickupD = models.DateField('Pickup date')
    returnD = models.DateField('Return date')

    def __str__(self):
        return ("%s - %s %s - %s" % (self.reservationNumber, self.customer.name, self.customer.surname, self.employee.email))


class ReservForm(models.Model):
    reservationID_temp = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cars = models.ManyToManyField(Car)
    pickupD = models.DateField('Pickup date')
    returnD = models.DateField('Return date')

    def __str__(self):
        return ("%s - %s" % (self.reservationID_temp,self.cars))

