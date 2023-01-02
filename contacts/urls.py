from django.urls import path
from . import views

urlpatterns = [
    path('fr_contact/', views.fr_contact, name='fr_contact'),
]
