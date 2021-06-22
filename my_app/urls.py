
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="about"),
    path('form/', views.form, name="form"),
    
]
