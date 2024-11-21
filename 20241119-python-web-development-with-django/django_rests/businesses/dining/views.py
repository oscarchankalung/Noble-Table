from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Restaurant

class RestaurantListView(ListView):
    model = Restaurant

class RestaurantDetailView(DetailView):
    model = Restaurant
