from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'app/home.html')


def wines(request):
	return render(request, 'app/wines.html')