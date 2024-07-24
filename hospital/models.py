from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=60)
    specialization = models.CharField(max_length=250)
    hospital_name = models.CharField(max_length=70)

    def __str__(self):
       return self.name
    
class Patient(models.Model):
    name = models.CharField(max_length=50)
    disease = models.CharField(max_length=200)
    medicines = models.TextField()    

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)  
    date1 = models.DateTimeField(default=None,null=True)

    def __str__(self):
        return self.doctor.name+"--"+self.patient.name
