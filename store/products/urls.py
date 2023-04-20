from django.urls import path, include

from .views import (CategoriesView, HomeView, ProductsView, basket_add,
                    basket_remove)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<str:slug>', CategoriesView.as_view(), name='categoriesview'),
    path('baskets/add/<int:product_id>', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>', basket_remove, name='basket_remove'),
]
