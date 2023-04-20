from django.urls import path
from orders.views import OrderCreateView,SuccessOrderView,CanceledOrderView

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('order-success/', SuccessOrderView.as_view(), name='order-success'),
    path('order-canceled/', CanceledOrderView.as_view(), name='order-canceled'),
]
