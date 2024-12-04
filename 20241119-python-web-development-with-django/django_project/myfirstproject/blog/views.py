from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post
from .forms import EmailForm

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

class EmailFormView(View):
    form_class = EmailForm
    template_name = "blog/form_email.html"
    success_url = "post_list"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form":form})
    
    def form_valid(self, form):
        form.send_email()
        return super(EmailFormView, self).form_valid()
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            print("valid")
            form.send_email()
            return HttpResponse("Email sent successfully")