from django.urls import path

from . import views

urlpatterns = [
    path('',views.AllEmployeData),
    path('add/',views.addEmploye),
    path('employe/<str:pk>/',views.EmployeDetail),
    path('Delemploye/<str:pk>/',views.EmployeDelete)
]
