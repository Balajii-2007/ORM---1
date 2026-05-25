from django.db import models

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    cuisine_type = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'food_restaurants'

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    CATEGORY_CHOICES = [
        ('STARTER', 'Starter'),
        ('MAIN', 'Main Course'),
        ('DESSERT', 'Dessert'),
        ('BEVERAGE', 'Beverage'),
    ]
    item_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_veg = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = 'food_items'

    def __str__(self):
        return f"{self.item_name} - {self.restaurant.name}"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=50)
    joined_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'food_customers'

    def __str__(self):
        return self.full_name


class DeliveryAgent(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('ON_DELIVERY', 'On Delivery'),
        ('OFFLINE', 'Offline'),
    ]
    agent_id = models.AutoField(primary_key=True)
    agent_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    vehicle_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AVAILABLE')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)

    class Meta:
        db_table = 'food_delivery_agents'

    def __str__(self):
        return self.agent_name


class Order(models.Model):
    STATUS_CHOICES = [
        ('PLACED', 'Order Placed'),
        ('CONFIRMED', 'Confirmed'),
        ('PREPARING', 'Preparing'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    delivery_agent = models.ForeignKey(DeliveryAgent, on_delete=models.SET_NULL, null=True, blank=True)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLACED')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    estimated_delivery = models.IntegerField(help_text="Estimated time in minutes", default=30)

    class Meta:
        db_table = 'food_orders'

    def __str__(self):
        return f"Order #{self.order_id} by {self.customer.full_name}"


class OrderItem(models.Model):
    orderitem_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'food_order_items'

    def subtotal(self):
        return self.quantity * self.item_price
