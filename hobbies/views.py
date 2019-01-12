from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Reservation, Employee, Car, Model, Customer, Position, ReservForm
from .forms import CustormerForm, CarForm, ReservationForm, ReservationApproved, PriceCalculator
from django.views.generic import TemplateView
from django.shortcuts import redirect


# Create your views here.
def index(request):
    reservations = Reservation.objects.order_by('-reservationNumber')[:5]
    employees = Employee.objects.order_by('-email')[:5]
    cars = Car.objects.order_by('-spz')[:5]
    models = Model.objects.order_by('-id')[:5]
    positions = Position.objects.order_by('-id')[:5]
    customers = Customer.objects.order_by('-driverLicense')[:5]
    reservform = ReservForm.objects.order_by('-reservationID_temp')[:5]
    context = {'reservations': reservations, 'employees': employees, 'cars': cars, 'models': models,
               'customers': customers, 'positions': positions, 'reservform': reservform}
    return render(request, 'polls/index.html', context)


def reserv_form(request):
    cars = Car.objects.order_by('-spz')[:5]
    return render(request, 'polls/forms/reservation.html', {'cars': cars})


# def reserv_forward(request):
# Reserv_form.customer =


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
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'polls/customer/detail.html', {'customer': customer})


def position_detail(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    return render(request, 'polls/position/detail.html', {'position': position})


##forms


def reservform_detail(request, resv_id):
    reservation = get_object_or_404(ReservForm, pk=resv_id)
    if request.method == 'POST':
        form = ReservationApproved(request.POST)
        form.customer = reservation.customer
        form.returnD = reservation.returnD
        form.pickupD = reservation.pickupD
        form.cars = reservation.cars
        if form.is_valid():
            form.save()
            ReservForm.objects.get(pk=resv_id).delete()
            return redirect('/hobbies/')
        else:
            return HttpResponse('<h1>ALREADY RESERVED</h1>')
    else:
        form = ReservationApproved()
        return render(request, 'polls/TempReservation/detail.html', {'reservation': reservation, 'form': form})


# Kdyz dorazime k tomuhle view s GET metodou, tak se vytvoří prázdná instance formu a uloží se contextu templatu a vyrenderuje se
# Kdyz s POST, tak vytvoří form a nahraje data z requestu

def registration(request):
    if request.method == 'POST':
        form = CustormerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hobbies/')
        else:
            return HttpResponse('<h1>ALREADY REGISTERED</h1>')
    else:
        form = CustormerForm()
        return render(request, 'polls/forms/CustomerRegistration.html', {'form': form})


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hobbies/')
        else:
            return HttpResponse('<h1>ALREADY IN DATABASE</h1>')
    else:
        form = CarForm()
        return render(request, 'polls/forms/AddCar.html', {'form': form})


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hobbies/')
        else:
            return HttpResponse('<h1>ALREADY RESERVED</h1>')
    else:
        form = ReservationForm()
        return render(request, 'polls/forms/reservation.html', {'form': form})


def calculator(request):
    result = 0
    cars = Car.objects.order_by('-spz')[:5]
    if request.method == 'POST':
        form = PriceCalculator(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            return calc_output(form)
        else:
            return HttpResponse('<h1>Something goes wrong...</h1>')
    else:
        form = PriceCalculator()
        return render(request, 'polls/forms/PriceCalculator.html', {'form': form, 'result': result, 'cars': cars})


def calc_output(form):
    if form.Dfrom == form.Dto:
        result = form.Dprice
    else:
        result = (form.Dto.day - form.Dfrom.day) * form.Dprice
    return HttpResponse('Finnal price: %s'% result)