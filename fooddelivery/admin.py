from django.contrib import admin
from .models import Restaurant, FoodItem, Customer, DeliveryAgent, Order, OrderItem

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['restaurant_id', 'name', 'location', 'cuisine_type', 'rating', 'is_active']
    list_filter = ['cuisine_type', 'is_active']
    search_fields = ['name', 'location']

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'item_name', 'restaurant', 'price', 'category', 'is_veg', 'is_available']
    list_filter = ['category', 'is_veg', 'is_available']
    search_fields = ['item_name']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'full_name', 'email', 'phone', 'city', 'joined_date']
    search_fields = ['full_name', 'email', 'phone']

@admin.register(DeliveryAgent)
class DeliveryAgentAdmin(admin.ModelAdmin):
    list_display = ['agent_id', 'agent_name', 'phone', 'vehicle_type', 'status', 'rating']
    list_filter = ['status', 'vehicle_type']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer', 'restaurant', 'order_status', 'total_amount', 'order_date']
    list_filter = ['order_status']
    search_fields = ['customer__full_name', 'restaurant__name']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['orderitem_id', 'order', 'food_item', 'quantity', 'item_price']
