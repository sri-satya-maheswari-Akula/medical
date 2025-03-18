from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']

        if Patient_register.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already registered'}) 
               
        hashed_password = make_password(password)       
        patient = Patient_register.objects.create(name=name, email=email, mobile=mobile, password=hashed_password)
        return redirect('login')

    return render(request, 'register.html')

def forget_password(request):
    return render(request, 'forgot-password.html')



#####################################  Doctor Dashboard #######################################


def doc_dashboard(request):
    return render(request, 'doctor-dashboard.html')
def appointments(request):
    return render(request, 'appointments.html')

def doc_register(request):
    return render(request, 'doctor-register.html')


######################################### Patient Dashboard ######################################

def search(request):
    return render(request,'search.html')