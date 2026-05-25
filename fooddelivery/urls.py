from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('customers/', views.customer_list, name='customer_list'),
    path('agents/', views.agent_list, name='agent_list'),
]
