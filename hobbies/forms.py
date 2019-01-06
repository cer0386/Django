from django import forms



class CustormerRegistration(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    surname = forms.CharField(label='Surname', max_length=50)
    driverLicense = forms.CharField(label='Driver License', max_length=8)
    email = forms.EmailField(label='Email')
    city = forms.CharField(label='City', max_length=50)
    street = forms.CharField(label='Street', max_length=50)
    houseNumber = forms.IntegerField(label='House Number')
