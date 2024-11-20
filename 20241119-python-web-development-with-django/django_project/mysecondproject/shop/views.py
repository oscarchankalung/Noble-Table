from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Car

def index(request):
    return HttpResponse("Hello World")

class CarListView(ListView):
    model = Car

class CarDetailView(DetailView):
    model = Car
