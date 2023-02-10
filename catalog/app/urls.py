from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = "app"

urlpatterns = [
	path('', views.home, name='home'),
	path('wines/', csrf_exempt(views.WinesView.as_view()), name='wines'),
	path('beers/', csrf_exempt(views.BeersView.as_view()), name='beers'),
]