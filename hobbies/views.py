from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Reservation, Employee

# Create your views here.
def index(request):
    reservations = Reservation.objects.order_by('-reservationNumber')[:5]
    employees = Employee.objects.order_by('-email')[:5]
    context = {'reservations': reservations, 'employees': employees}
    return render(request, 'polls/index.html', context)

def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    return render(request, 'polls/reservation_detail.html', {'reservation': reservation})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'polls/employee_detail.html', {'employee': employee})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)