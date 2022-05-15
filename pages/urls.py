from importlib.resources import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about/', views.about, name='about'),
    path('adminarea/',views.adminArea, name='adminArea'),
]