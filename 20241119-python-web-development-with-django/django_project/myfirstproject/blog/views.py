from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post

def index(request):
    message = "Hey this is my Blog app!"
    return render(request, "blog/hello.html", {"template_message": message})

class PostListView(ListView):
    model = Post
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content", "slug", "image"]
    success_url = reverse_lazy("post_list")
    template_name = "blog/post_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Post"
        context["heading"] = "Create your Post"
        context["button_value"] = "Create"
        return context

class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content", "slug", "image"]
    success_url = reverse_lazy("post_list")
    template_name = "blog/post_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Post"
        context["heading"] = f"Update your Post: {self.object.title}"
        context["button_value"] = "Update"
        return context

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")