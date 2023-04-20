from django.contrib import admin

from .models import Products, ProductsCategory


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'price', 'quantity', 'image', 'slug', 'category', ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProductsCategory)
class ProductsCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'slug', ]
    prepopulated_fields = {'slug': ('title',)}
