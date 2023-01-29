from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Car
# Create your views here.

class home(ListView):
    model = Car
    template_name = 'home.html'    

def login(request):
    return render(request, 'login.html', {})

def add_car(request):
    return render(request, 'add_car.html', {})

class car_details(DetailView):
    model = Car
    template_name = 'car_details.html'
    fields = '__all__'