from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('branding', views.branding, name='branding'),
    path('illustration', views.illustration, name='illustration'),
    path('full-package', views.fullpackage, name='full-package'),
    path('website', views.website, name='website'),
]
