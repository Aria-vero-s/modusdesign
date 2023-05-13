from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('templates', views.html_template_products, name='templates'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('template/<int:product_id>', views.template_detail, name='template_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),
]