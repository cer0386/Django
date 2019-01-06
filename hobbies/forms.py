from django import forms
from .models import Customer, Car, Model



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

class CarForm(forms.ModelForm):
    spz = forms.CharField(label='SPZ', max_length=7)
    model = forms.ModelChoiceField(label='Car Model', queryset=Model.objects.all())
    bought = forms.DateField(label='Date of purchase')
    stk = forms.DateField(label='STK expiracy')
    nOAccidents = forms.IntegerField(label='Number of accidents')

    class Meta:
        model = Car
        fields = '__all__'

