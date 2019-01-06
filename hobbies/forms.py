from django import forms
from .models import Customer, ReservForm, Car


class CustormerForm(forms.ModelForm):
    driverLicense = forms.CharField(label='Driver License', max_length=8)
    name = forms.CharField(label='Name', max_length=50)
    surname = forms.CharField(label='Surname', max_length=50)
    email = forms.EmailField(label='Email')
    city = forms.CharField(label='City', max_length=50)
    street = forms.CharField(label='Street', max_length=50)
    houseNumber = forms.IntegerField(label='House Number')

    class Meta:
        model = Customer
        fields = '__all__'


class ReservationForm(forms.ModelForm):
    reservationID_temp = forms.IntegerField(label='Reservation ID')
    customer = forms.ModelMultipleChoiceField(queryset=Customer.objects.all())
    cars = forms.ModelMultipleChoiceField(queryset=Car.objects.all())
    pickupD = forms.DateField(label='Pickup')
    returnD = forms.DateField(label='Return')

    class Meta:
        model = ReservForm
        fields = '__all__'

