from django.urls import path
from . import views

urlpatterns = [
	path('fr_request_form/', views.fr_request_form, name='fr_request_form'),
]