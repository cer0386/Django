from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Reservation

# Create your views here.
def index(request):
    list = Reservation.objects.order_by('-reservationNumber')[:5]
    context = {'list': list}
    return render(request, 'polls/index.html', context)

def detail(request, e_id):
    e = get_object_or_404(Reservation, pk=e_id)
    return render(request, 'polls/detail.html', {'e': e})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)