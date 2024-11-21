from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200, unique=False, blank=False)
    rating = models.FloatField(null=True) # 0.0-5.0 or null
    review_count = models.IntegerField(null=True) # 0-9999 or null
    price = models.IntegerField(null=True) # 0-3 or null
    cuisine = models.CharField(max_length=200, blank=True) # 'French' or blank
    image = models.ImageField(upload_to="uploads/", blank=True) # object or blank
    address = models.CharField(max_length=200, blank=True) # '145 W 53rd St' or blank
    city = models.CharField(max_length=200, blank=True) # 'New  York' or blank
    zip_code = models.CharField(max_length=5, blank=True) # '12345' or blank
    state = models.CharField(max_length=2, blank=True) # 'NY' or blank
    phone = models.CharField(max_length=14, blank=True) # '(212) 510-7714' or blank

    def __str__(self):
        return f"{self.name}, {self.city}"