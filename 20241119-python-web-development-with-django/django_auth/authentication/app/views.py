from django.shortcuts import render

def base_view(request):
    context = {"message": "This is base message", "number": 100}
    return render(request, "base.html", context)
  
def child_apple_view(request):
    context = {"message": "This is child apple message", "number": 200}
    return render(request, "child_apple.html", context)

def child_orange_view(request):
    context = {"message": "This is child orange message", "number": 300}
    return render(request, "child_orange.html", context)
