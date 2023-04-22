from django.urls import path

from orders.views import (CanceledOrderView, OrderCreateView, OrderDetailView,
                          OrderListView, SuccessOrderView)

urlpatterns = [
    path('', OrderListView.as_view(), name='orders'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('order-success/', SuccessOrderView.as_view(), name='order-success'),
    path('order-canceled/', CanceledOrderView.as_view(), name='order-canceled'),
]
