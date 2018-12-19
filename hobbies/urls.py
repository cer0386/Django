from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),
    path('<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>', views.vote, name='create'),
]