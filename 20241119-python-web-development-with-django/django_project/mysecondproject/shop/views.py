from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Car

def index(request):
    return HttpResponse("Hello World")

class CarListView(ListView):
    model = Car

class CarDetailView(DetailView):
    model = Car

class CarCreateView(CreateView):
    model = Car
    fields = ["make", "model", "year", "description", "image", "slug"]
    success_url = reverse_lazy("car_list")
    template_name = "shop/car_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Car"
        context["heading"] = "Create your Car"
        context["button_value"] = "Create"
        return context

class CarUpdateView(UpdateView):
    model = Car
    fields = ["make", "model", "year", "description", "image", "slug"]
    success_url = reverse_lazy("car_list")
    template_name = "shop/car_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Car"
        context["heading"] = "Update your Car"
        context["button_value"] = "Update"
        return context

class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy("car_list")