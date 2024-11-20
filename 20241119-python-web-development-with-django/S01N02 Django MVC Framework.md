# Django MVC Framework

## Framework

- MVC
- model > model
- views > controller
- template > view to be created

1. Create a model on `{project}/{app}/models.py`
1. Create a view on `{project}/{app}/views.py`
1. Add url pattern on `{project}/{core}/urls.py`
1. Add template on `{project}/{app}/templates/app/{object}.html`

## Model

### `{project}/{app}/models.py`

```py
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
```

### `{project}/{app}/admin.py`

```py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

```bash
# create database migration after creating new model(s)
python manage.py makemigrations

# update database
python manage.py migrate
```

## View as Controller 

### `{project}/{app}/views.py`

```py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post

def index(request):
    message = "Hey this is my Blog app!"
    return render(request, "blog/hello.html", {"template_message": message})

class PostListView(ListView):
    model = Post
    
class PostDetailView(DetailView):
    model = Post
```

## Template as View

### `{project}/{app}/templates/{app}/object_list.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Post List</title>
</head>
<body>
  <h1>Posts</h1>
  {% for object in object_list %}
  <h3>
    <a href={{ object.get_absolute_url }}>{{ object.title }}</a>
  </h3>
  {% endfor %}
</body>
</html>
```

### `{project}/{app}/templates/{app}/object_detail.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Post Detail</title>
</head>
<body>
  <h1>{{ object.title }}</h1>
  <h3>{{ object.content }}</h3>
  <h3>{{ object.slug }}</h3>
  {% if object.image %}
    <img src="{{ object.image.url }}" alt="{{ object.title }}">
  {% endif %}
  <a href={% url "post_list" %}>
    <button type="button">Go back to list</button>
  </a>
</body>
</html>
```

### `{project}/{core}/urls.py`

```py
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", views.index),
    path("", views.PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```