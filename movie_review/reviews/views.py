from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Review


class HomePageView(ListView):
    template_name = "home.html"
    model = Review
