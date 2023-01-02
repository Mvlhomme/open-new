from django.urls import path
from . import views

urlpatterns = [
	path('fr_mabanque/', views.fr_mabanque, name='fr_mabanque'),
]