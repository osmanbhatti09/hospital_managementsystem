from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('view_doctor/', views.view_doctor, name="view_doctor"),
    path('view_patient/', views.view_patient, name="view_patient"),
    path('view_appointment/', views.view_appointment, name="view_appointment"),
    path('add_doctor/', views.add_doctor, name="add_doctor"),
    path('delete_doctor/<int:id>', views.delete_doctor, name="delete_doctor"),
    path('add_patient/', views.add_patient, name="add_patient"),
    path('delete_patient/<int:id>', views.delete_patient, name="delete_patient"),
    path('add_appointment/', views.add_appointment, name="add_appointment"),
    path('delete_appointment/<int:id>', views.delete_appointment, name="delete_appointment"),
]
