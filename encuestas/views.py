# Django
from django.shortcuts import render
from django.views.generic import DetailView

# Models


# Forms


def HomeView(request):
    return render(request, "home.html")


