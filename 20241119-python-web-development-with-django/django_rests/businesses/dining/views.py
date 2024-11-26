from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from .models import Restaurant

def index(request):
    return HttpResponse("index")

class RestaurantListView(ListView):
    model = Restaurant

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        restaurants = context["object_list"]
        cities = set([r.city for r in restaurants])
        
        context["title"] = "All Restaurants"
        context["cities"] = cities
        context["number_of_restaurant"] = len(restaurants)
        return context

class RestaurantFilterCityView(ListView):
    model = Restaurant
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        restaurants = context["object_list"]
        cities = set([r.city for r in restaurants])
        
        city = self.kwargs["city"].lower()
        city = " ".join([w.capitalize() for w in city.split()])
        filtered_restaurants = restaurants.filter(city__icontains = city)
        
        context["title"] = f"Restaurants in {city}"
        context["cities"] = cities
        context["city"] = city
        context["number_of_restaurant"] = len(filtered_restaurants)
        context["object_list"] = filtered_restaurants
        return context

class RestaurantDetailView(DetailView):
    model = Restaurant