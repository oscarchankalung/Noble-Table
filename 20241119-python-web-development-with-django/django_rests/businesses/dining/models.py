from django.urls import reverse
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200, unique=False, blank=False)
    rating = models.FloatField(null=True) # 0.0-5.0 or null
    review_count = models.IntegerField(null=True) # 0-9999 or null
    price = models.IntegerField(null=True) # 0-3 or null
    cuisine = models.CharField(max_length=200, blank=True) # 'French' or ''
    image = models.ImageField(upload_to="uploads/", blank=True) # object or ''
    address = models.CharField(max_length=200, blank=True) # '145 W 53rd St' or ''
    city = models.CharField(max_length=200, blank=True) # 'New  York' or ''
    zip_code = models.CharField(max_length=5, blank=True) # '12345' or ''
    state = models.CharField(max_length=2, blank=True) # 'NY' or ''
    phone = models.CharField(max_length=14, blank=True) # '(212) 510-7714' or ''

    def __str__(self):
        return f"{self.name}, {self.city}"
    
    def get_absolute_url(self):
        return reverse("restaurant_detail", kwargs={"pk": self.pk})

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    rating = models.FloatField(null=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.restaurant}, {self.rating}, {self.comment[:10]}"