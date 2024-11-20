from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200, unique=False, blank=False)
    content = models.TextField(max_length=500)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="uploads/", blank=True)
    
    def __str__(self):
        return f"{self.title}, {self.slug}"
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    