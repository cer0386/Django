from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Reservation, Employee, Car, Model, Customer, Position

# Create your views here.
def index(request):
    reservations = Reservation.objects.order_by('-reservationNumber')[:5]
    employees = Employee.objects.order_by('-email')[:5]
    cars = Car.objects.order_by('-spz')[:5]
    models = Model.objects.order_by('-id')[:5]
    positions = Position.objects.order_by('-id')[:5]
    customers = Customer.objects.order_by('-driverLicense')[:5]
    context = {'reservations': reservations, 'employees': employees, 'cars': cars, 'models': models,
               'customers': customers, 'positions': positions}
    return render(request, 'polls/index.html', context)

def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    return render(request, 'polls/reservation/detail.html', {'reservation': reservation})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'polls/employee/detail.html', {'employee': employee})

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'polls/car/detail.html', {'car': car})

def model_detail(request, model_id):
    model = get_object_or_404(Model, pk=model_id)
    return render(request, 'polls/model/detail.html', {'model': model})

def customer_detail(request, customer_id):
    customer = get_object_or_404(Model, pk=customer_id)
    return render(request, 'polls/customer/detail.html', {'customer': customer})

def position_detail(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    return render(request, 'polls/position/detail.html', {'position': position})
