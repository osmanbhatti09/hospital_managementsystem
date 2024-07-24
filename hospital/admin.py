from django.contrib import admin
from . models import Doctor,Patient,Appointment
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','specialization','hospital_name']

class PatientAdmin(admin.ModelAdmin):
    list_display = ['name','disease','medicines']

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor','patient','date1']


admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Appointment,AppointmentAdmin)