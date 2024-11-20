# Django CRUD

## [Generic editing views](https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-editing/)

1. `CreateView`
1. `UpdateView`
1. `DeleteView`

### `{project}/{app}/views.py`

```py
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
```

### `{project}/{app}/urls.py`

```py
urlpatterns = [
    ...,
    path("post/create/", views.PostCreateView.as_view(), name="post_create"),
    path("post/update/<int:pk>/", views.PostUpdateView.as_view(), name="post_update"),
    path("post/delete/<int:pk>/", views.PostDeleteView.as_view(), name="post_delete"),
]
```
### `{project}/{app}/templates/{app}/post_list.html`

```html
<p><a href={% url "post_create" %}><button type="button">Create Post</button></a></p>
```

### `{project}/{app}/templates/{app}/post_detail.html`

```html
<p><a href={% url "post_update" pk=object.id %}><button type="button">Update Post</button></a></p>
<p><a href={% url "post_delete" pk=object.id %}><button type="button">Delete Post</button></a></p>
```

### `{project}/{app}/templates/{app}/post_form.html`

```html
<h1>{{ heading }}</h1>
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value=" {{ button_value }}">
</form>
```

### `{project}/{app}/templates/{app}/post_confirm_delete.html`

```html
<form method="post">
    {% csrf_token %}
    <p>Are you sure you want to delete "{{ object }}"?</p>
    {{ form }}
    <input type="submit" class="btn btn-danger" value="Confirm">
</form>
<p><a href={% url "post_detail" pk=object.id %}><button type="button" class="btn btn-warning">Cancel</button></a></p>
```

## Cross-Site Request Forgery (CSRF)

## `reverse()` and `reverse_lazy()`

Use reverse() for immediate URL resolution during runtime.
Use reverse_lazy() for deferred URL resolution, typically required in class-based attributes or settings where premature URL access may cause issues.

## Virtual DOM

No, Django's templating system doesn't use a virtual DOM.
Here's why:
Django's Templating Engine:
Django's built-in templating language (DTL) is server-side rendered, which means it generates HTML on the server and sends it to the client. This is different from client-side rendering, where JavaScript frameworks like React or Vue use a virtual DOM to manage updates.