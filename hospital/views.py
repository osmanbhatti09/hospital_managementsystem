from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.
def home(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors =Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()
    doc = 0;
    pat = 0;
    appoin = 0;
    for i in doctors:
        doc +=1
    for i in patients:
        pat +=1
    for i in appointments:
        appoin +=1         
    dict = {'doc':doc,'pat':pat,'appoin':appoin}    
    return render(request,'home.html',dict)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    error=""
    if request.method == "Post":
        unam = request.Post['username']
        upass = request.Post['pwd']
        user = authenticate(username=unam, password=upass)
        try:
            if  request.user.is_staff:
                 login(request,user)
                 error="no"
            else:
                error = "yes"
        except:
              error = "yes" 
    d = {'error':error}                              
    return render(request,'login.html',d)

def user_logout(request):
    logout(request)
    return redirect('login')

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doctor =Doctor.objects.all()
    doc = {'doctor':doctor}
    return render(request, 'view_doctor.html', doc)

def view_patient(request):
    if not request.user.is_staff:
        return render('login')
    patient= Patient.objects.all()
    patn = {'patient':patient}
    return render(request, 'view_patient.html', patn)

def view_appointment(request):
    if not request.user.is_staff:
        return render('login')
    appointment =Appointment.objects.all()
    appoint = {'appointment':appointment}
    return render(request, 'view_appointment.html', appoint)

def add_doctor(request):
    error =""
    if request.method == "POST":

        unam = Doctor.POST['name']
        specal = Doctor.POST['specialization']
        hosp_nme = Doctor.POST['hopital_name']
        try:
            Doctor.objects.create(name=unam,specialization=specal,hospital_name=hosp_nme)
            error = "no"
        except:
              error = "yes" 
    dict = {'error':error}                     
    return render(request, 'add_doctor.html',dict)

def delete_doctor(request,id):
    if not request.user.is_staff:
        return redirect('/login')
    var = Doctor.objects.get(pk=id)
    var.delete()
    return redirect('view_doctor')

def add_patient(request):
    error = ""
    if request.method == "POST":
        unam = Patient.POST['name']
        dises = Patient.POST['disease']
        gend = Patient.POST['gender']
        medi = Patient.POST['medicines']
        try:
            Patient.objects.create(name=unam,disease=dises,gender=gend, medicines=medi)
            error = "no"
        except:
            error = "yes"    
    dict = {'error':error}        
    return render(request, 'add_patient.html',dict)

def delete_patient(request,id):
    if not request.user.is_staff:
        return redirect('/login')
    patent = Patient.objects.get(pk=id)
    patent.delete()
    return redirect('view_patient')

def add_appointment(request):
    error = ""
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    if request.method == "POST":
        doc = Patient.POST['doctor']
        paten = Patient.POST['patient']
        dt1 = Patient.POST['date1']
        doctor1 = Doctor.objects.filter(name=doc).first()
        patient1 = Patient.objects.filter(name=paten).first()
        try:
            Appointment.objects.create(doctor=doctor1,patient=patient1,date1=dt1)
            error = "no"
        except:
            error = "yes"    
    dict = {'doctor1':doctor,'patient1':patient ,'error':error}        
    return render(request, 'add_appointment.html',dict)

def delete_appointment(request,id):
    if not request.user.is_staff:
        return redirect('/login')
    appoint = Appointment.objects.get(pk=id)
    appoint.delete()
    return redirect('view_appointment')
