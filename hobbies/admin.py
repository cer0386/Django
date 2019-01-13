from django.contrib import admin
from .models import Customer,Car,Employee,Reservation,Model,Position, ReservForm, Comment

# Register your models here.
admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Comment)
admin.site.register(Employee)
admin.site.register(Reservation)
admin.site.register(Model)
admin.site.register(Position)
admin.site.register(ReservForm)
