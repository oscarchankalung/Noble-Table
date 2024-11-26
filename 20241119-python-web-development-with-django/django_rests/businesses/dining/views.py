from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from rest_framework import generics

from .models import Restaurant
from .serializers import RestaurantListSerializer, RestaurantDetailSerializer

'''
API Views
'''

class RestaurantListAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer

class RestaurantDetailAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer

'''
Template Views
'''

def index(request):
    return HttpResponse("index")

class RestaurantListView(ListView):
    model = Restaurant

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        restaurants = context["object_list"]
        cities = set([r.city for r in restaurants])
        cuisines = set([r.cuisine for r in restaurants])
        
        context["title"] = "All Restaurants"
        context["cities"] = cities
        context["cuisines"] = cuisines
        context["number_of_restaurant"] = len(restaurants)
        return context

class RestaurantSearchView(ListView):
    model = Restaurant

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        city = self.request.GET.get("city") or self.kwargs.get("city")
        cuisine = self.request.GET.get("cuisine") or self.kwargs.get("cuisine")
        url_name = self.request.resolver_match.url_name

        print(url_name, city, cuisine)

        restaurants = context["object_list"]
        filtered_restaurants = restaurants

        # kwargs and request 
        if city:
            filtered_restaurants = restaurants.filter(city__icontains = city)
        if cuisine:
            filtered_restaurants = restaurants.filter(cuisine__icontains = cuisine)
        
        # kwargs
        if url_name == "restaurant_city":
            context["cities"] = set([r.city for r in restaurants])
        if url_name == "restaurant_cuisine":
            context["cuisines"] = set([r.cuisine for r in restaurants])

        context["title"] = "Restaurants Search"
        context["city"] = city
        context["cuisine"] = cuisine
        context["number_of_restaurant"] = len(filtered_restaurants)
        context["object_list"] = filtered_restaurants
        return context

class RestaurantDetailView(DetailView):
    model = Restaurant
