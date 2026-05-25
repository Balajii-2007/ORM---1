from django.shortcuts import render, get_object_or_404
from .models import Restaurant, FoodItem, Customer, DeliveryAgent, Order, OrderItem


def dashboard(request):
    context = {
        'total_restaurants': Restaurant.objects.count(),
        'total_orders': Order.objects.count(),
        'total_customers': Customer.objects.count(),
        'total_agents': DeliveryAgent.objects.count(),
        'recent_orders': Order.objects.select_related('customer', 'restaurant').order_by('-order_date')[:5],
        'restaurants': Restaurant.objects.all(),
    }
    return render(request, 'fooddelivery/dashboard.html', context)


def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'fooddelivery/restaurant_list.html', {'restaurants': restaurants})


def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    menu_items = FoodItem.objects.filter(restaurant=restaurant)
    return render(request, 'fooddelivery/restaurant_detail.html', {
        'restaurant': restaurant,
        'menu_items': menu_items
    })


def order_list(request):
    orders = Order.objects.select_related('customer', 'restaurant', 'delivery_agent').order_by('-order_date')
    return render(request, 'fooddelivery/order_list.html', {'orders': orders})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    items = OrderItem.objects.filter(order=order).select_related('food_item')
    return render(request, 'fooddelivery/order_detail.html', {'order': order, 'items': items})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'fooddelivery/customer_list.html', {'customers': customers})


def agent_list(request):
    agents = DeliveryAgent.objects.all()
    return render(request, 'fooddelivery/agent_list.html', {'agents': agents})
