from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.home, name="index"),
    path('about/', views.about, name='about'),
    path('search/', views.search,name="search"),
    path('forms/', views.forms, name='form')
]