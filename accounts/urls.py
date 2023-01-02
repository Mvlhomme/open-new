from django.urls import path
from . import views

urlpatterns = [
    # Inscription, connextion et rénitialition
    path('fr_register/', views.fr_register, name='fr_register'),
    path('fr_reset/', views.fr_reset, name='fr_reset'),
    path('fr_login/', views.fr_login, name='fr_login'),
    path('fr_logout/', views.fr_logout, name='fr_logout'),

    #Accès au tableau de bord
    path('fr_profile/', views.fr_profile, name='fr_profile'),
    path('fr_dashboard/', views.fr_dashboard, name='fr_dashboard'),
    path('', views.fr_dashboard, name='fr_dashboard'),
]