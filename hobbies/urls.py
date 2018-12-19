from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('customer/<slug:customer_id>/', views.customer_detail, name='customer_detail'),
    path('reservation/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('model/<int:model_id>/', views.model_detail, name='model_detail'),
    path('position/<int:position_id>/', views.position_detail, name='position_detail'),
]
