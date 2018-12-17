from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20)
    joined = models.DateField('Joined community')
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.surname

class Product(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    width = models.IntegerField()
    height = models.DecimalField(max_digits=10, decimal_places=2)
    depth = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added = models.DateTimeField('Product published')

    def __str__(self):
        return self.name + ' ' + self.description

    def publishedRecently(self):
        return self.added >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    added = models.DateTimeField('Added Comment')

    def __str__(self):
        return self.product + ' ' + self.text + ' ' + self.user

class Ranking(models.Model):
    rankingIntValue = models.IntegerField(default=5)
    text = models.CharField(max_length=20)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.text


