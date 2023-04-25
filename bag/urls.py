from django.urls import path
from . import views

urlpatterns = [
    path('quote', views.quote, name='quote'),
    path('', views.view_bag, name='view_bag'),
    path('bag/add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('test', views.test, name='test'),
    path('quoteslides', views.quoteslides, name='quoteslides'),
]