from django.shortcuts import render
from django.http import HttpResponse
from car.models import Registration

def pg(request):
    return render(request,"car/pg.html")

def log(request):
    return render(request,"car/lg.html")

def sup(request):
    return render(request,"car/signup.html")

def registered(request):
    first_name = request.POST['fn']
    last_name = request.POST['ln']
    email = request.POST['email']
    password = request.POST['password']

    person = Registration(first_name=first_name, last_name=last_name, email=email, password=password)
    person.save()
    return render(request,"car/registered.html",{'fn':first_name})