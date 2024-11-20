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