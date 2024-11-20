from django.db import models
from django.urls import reverse

class Car(models.Model):
    make = models.CharField(max_length=100, unique=False, blank=False)
    model = models.CharField(max_length=100, unique=False, blank=False)
    year = models.DateField()
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="uploads/", blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.make} / {self.model} / {self.year.year}"
    
    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})
    