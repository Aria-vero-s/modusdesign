from django.urls import path
from . import views

app_name = 'bag'

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('quoteslides/', views.quoteslides, name='quoteslides'),
    path('add_to_bag/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('quote/', views.quote, name='quote'),
    path('test/', views.test, name='test'),
]