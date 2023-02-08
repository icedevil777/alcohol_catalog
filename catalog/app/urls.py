from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
	path('', views.home, name='home'),
	path('wines/', views.wines, name='wines'),
]