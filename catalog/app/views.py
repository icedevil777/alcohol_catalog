from django.views.generic import ListView
from .models import Wine
from django.shortcuts import render


def home(request):
    return render(request, 'app/home.html')


class WinesView(ListView):
    """Wine objects"""
    model = Wine
    template_name = 'app/wines.html'


