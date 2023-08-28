from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('branding', views.branding, name='branding'),
    path('website', views.website, name='website'),
    path('illustration', views.illustration, name='illustration'),
    path('terms', views.terms, name='terms'),
    path('', views.index, name='index'),
]