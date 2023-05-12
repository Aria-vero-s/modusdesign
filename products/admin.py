from django.contrib import admin
from .models import Product, Category, Template

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class TemplateAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'image_url',
        'image',
        'category',
        'price',
        'quantity',
        'sku',
    )

    ordering = ('sku',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Template, TemplateAdmin)