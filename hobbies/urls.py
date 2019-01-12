from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('forms/reservation/', views.reservation, name='reservation'),
    path('forms/CustomerRegistration/', views.registration, name='registration'),
    path('forms/AddCar/', views.add_car, name='add_car'),
    path('forms/AddModel/', views.add_car, name='add_model'),
    #path('forms/PriceCalculator/', views.calculator, name='calculator'),
    path('car/<slug:car_id>/', views.car_detail, name='car_detail'),
    path('customer/<slug:customer_id>/', views.customer_detail, name='customer_detail'),
    path('reservation/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('model/<int:model_id>/', views.model_detail, name='model_detail'),
    path('position/<int:position_id>/', views.position_detail, name='position_detail'),
    path('TempReservation/<int:resv_id>/', views.reservform_detail, name='reservform_detail'),
]
