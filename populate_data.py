import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodorm.settings')
django.setup()

from fooddelivery.models import Restaurant, FoodItem, Customer, DeliveryAgent, Order, OrderItem
from decimal import Decimal

print("🍕 Populating FoodORM database...")

# Clear existing data
OrderItem.objects.all().delete()
Order.objects.all().delete()
FoodItem.objects.all().delete()
Customer.objects.all().delete()
DeliveryAgent.objects.all().delete()
Restaurant.objects.all().delete()

# --- Restaurants (10 records) ---
restaurants = [
    Restaurant(name="Spice Garden", location="Anna Nagar, Chennai", cuisine_type="North Indian", rating=4.5),
    Restaurant(name="Pizza Palace", location="T. Nagar, Chennai", cuisine_type="Italian", rating=4.2),
    Restaurant(name="Dragon Wok", location="Adyar, Chennai", cuisine_type="Chinese", rating=4.3),
    Restaurant(name="Biryani Hub", location="Velachery, Chennai", cuisine_type="Mughlai", rating=4.7),
    Restaurant(name="Burger Barn", location="OMR, Chennai", cuisine_type="Fast Food", rating=4.0),
    Restaurant(name="Dosa Corner", location="Mylapore, Chennai", cuisine_type="South Indian", rating=4.6),
    Restaurant(name="Sushi Street", location="Nungambakkam, Chennai", cuisine_type="Japanese", rating=4.4),
    Restaurant(name="Kerala Kitchen", location="Tambaram, Chennai", cuisine_type="Kerala", rating=4.5),
    Restaurant(name="Taco Town", location="Guindy, Chennai", cuisine_type="Mexican", rating=4.1),
    Restaurant(name="The Grill House", location="Porur, Chennai", cuisine_type="Continental", rating=4.3),
]
Restaurant.objects.bulk_create(restaurants)
r = list(Restaurant.objects.all())
print(f"✅ Created {len(r)} restaurants")

# --- Food Items ---
food_items = [
    FoodItem(restaurant=r[0], item_name="Paneer Butter Masala", description="Creamy cottage cheese curry", price=220, category="MAIN", is_veg=True),
    FoodItem(restaurant=r[0], item_name="Dal Makhani", description="Slow-cooked black lentils", price=180, category="MAIN", is_veg=True),
    FoodItem(restaurant=r[1], item_name="Margherita Pizza", description="Classic tomato and mozzarella", price=299, category="MAIN", is_veg=True),
    FoodItem(restaurant=r[1], item_name="Pepperoni Pizza", description="Spicy pepperoni slices", price=349, category="MAIN", is_veg=False),
    FoodItem(restaurant=r[2], item_name="Chicken Fried Rice", description="Wok-tossed rice with chicken", price=199, category="MAIN", is_veg=False),
    FoodItem(restaurant=r[3], item_name="Chicken Biryani", description="Aromatic basmati rice with chicken", price=280, category="MAIN", is_veg=False),
    FoodItem(restaurant=r[3], item_name="Mutton Biryani", description="Slow-cooked mutton biryani", price=350, category="MAIN", is_veg=False),
    FoodItem(restaurant=r[4], item_name="Classic Burger", description="Beef patty with lettuce and cheese", price=149, category="MAIN", is_veg=False),
    FoodItem(restaurant=r[5], item_name="Masala Dosa", description="Crispy dosa with potato filling", price=80, category="MAIN", is_veg=True),
    FoodItem(restaurant=r[5], item_name="Filter Coffee", description="Traditional South Indian filter coffee", price=40, category="BEVERAGE", is_veg=True),
    FoodItem(restaurant=r[6], item_name="Salmon Sushi Roll", description="Fresh salmon with avocado", price=420, category="STARTER", is_veg=False),
    FoodItem(restaurant=r[7], item_name="Kerala Fish Curry", description="Spicy fish curry in coconut milk", price=260, category="MAIN", is_veg=False),
]
FoodItem.objects.bulk_create(food_items)
print(f"✅ Created {FoodItem.objects.count()} food items")

# --- Customers (10 records) ---
customers = [
    Customer(full_name="Arjun Sharma", email="arjun@email.com", phone="9876543210", address="12 MG Road", city="Chennai"),
    Customer(full_name="Priya Venkat", email="priya@email.com", phone="9876543211", address="45 Anna Nagar", city="Chennai"),
    Customer(full_name="Karthik Rajan", email="karthik@email.com", phone="9876543212", address="78 T. Nagar", city="Chennai"),
    Customer(full_name="Sneha Iyer", email="sneha@email.com", phone="9876543213", address="23 Adyar", city="Chennai"),
    Customer(full_name="Rahul Kumar", email="rahul@email.com", phone="9876543214", address="56 Velachery", city="Chennai"),
    Customer(full_name="Divya Nair", email="divya@email.com", phone="9876543215", address="89 OMR", city="Chennai"),
    Customer(full_name="Vijay Anand", email="vijay@email.com", phone="9876543216", address="34 Mylapore", city="Chennai"),
    Customer(full_name="Lakshmi Suresh", email="lakshmi@email.com", phone="9876543217", address="67 Nungambakkam", city="Chennai"),
    Customer(full_name="Arun Prasad", email="arun@email.com", phone="9876543218", address="90 Tambaram", city="Chennai"),
    Customer(full_name="Meena Krishnan", email="meena@email.com", phone="9876543219", address="11 Guindy", city="Chennai"),
]
Customer.objects.bulk_create(customers)
c = list(Customer.objects.all())
print(f"✅ Created {len(c)} customers")

# --- Delivery Agents (10 records) ---
agents = [
    DeliveryAgent(agent_name="Suresh Kumar", phone="9111111110", vehicle_type="Bike", status="AVAILABLE", rating=4.8),
    DeliveryAgent(agent_name="Ravi Shankar", phone="9111111111", vehicle_type="Bike", status="ON_DELIVERY", rating=4.5),
    DeliveryAgent(agent_name="Murugan P", phone="9111111112", vehicle_type="Scooter", status="AVAILABLE", rating=4.7),
    DeliveryAgent(agent_name="Selva Raja", phone="9111111113", vehicle_type="Bike", status="AVAILABLE", rating=4.6),
    DeliveryAgent(agent_name="Dinesh T", phone="9111111114", vehicle_type="Scooter", status="OFFLINE", rating=4.4),
    DeliveryAgent(agent_name="Prem Kumar", phone="9111111115", vehicle_type="Bike", status="AVAILABLE", rating=4.9),
    DeliveryAgent(agent_name="Balu S", phone="9111111116", vehicle_type="Bicycle", status="ON_DELIVERY", rating=4.3),
    DeliveryAgent(agent_name="Vikram N", phone="9111111117", vehicle_type="Bike", status="AVAILABLE", rating=4.7),
    DeliveryAgent(agent_name="Saravanan K", phone="9111111118", vehicle_type="Scooter", status="AVAILABLE", rating=4.5),
    DeliveryAgent(agent_name="Manoj R", phone="9111111119", vehicle_type="Bike", status="ON_DELIVERY", rating=4.6),
]
DeliveryAgent.objects.bulk_create(agents)
a = list(DeliveryAgent.objects.all())
print(f"✅ Created {len(a)} delivery agents")

# --- Orders (10 records) ---
fi = list(FoodItem.objects.all())
orders_data = [
    (c[0], r[0], a[0], "DELIVERED",   460.00, "12 MG Road, Chennai"),
    (c[1], r[1], a[1], "OUT_FOR_DELIVERY", 299.00, "45 Anna Nagar, Chennai"),
    (c[2], r[3], a[2], "PREPARING",   280.00, "78 T. Nagar, Chennai"),
    (c[3], r[2], a[3], "CONFIRMED",   199.00, "23 Adyar, Chennai"),
    (c[4], r[4], a[0], "DELIVERED",   149.00, "56 Velachery, Chennai"),
    (c[5], r[5], a[5], "DELIVERED",   120.00, "89 OMR, Chennai"),
    (c[6], r[6], a[6], "PLACED",      420.00, "34 Mylapore, Chennai"),
    (c[7], r[7], a[7], "PREPARING",   260.00, "67 Nungambakkam, Chennai"),
    (c[8], r[3], a[8], "DELIVERED",   630.00, "90 Tambaram, Chennai"),
    (c[9], r[9], a[9], "CANCELLED",   350.00, "11 Guindy, Chennai"),
]

for cust, rest, agent, status, amount, addr in orders_data:
    Order.objects.create(
        customer=cust, restaurant=rest, delivery_agent=agent,
        order_status=status, total_amount=Decimal(str(amount)),
        delivery_address=addr, estimated_delivery=30
    )
orders = list(Order.objects.all())
print(f"✅ Created {len(orders)} orders")

# --- Order Items ---
order_items = [
    OrderItem(order=orders[0], food_item=fi[0], quantity=1, item_price=fi[0].price),
    OrderItem(order=orders[0], food_item=fi[1], quantity=1, item_price=fi[1].price),
    OrderItem(order=orders[1], food_item=fi[2], quantity=1, item_price=fi[2].price),
    OrderItem(order=orders[2], food_item=fi[5], quantity=1, item_price=fi[5].price),
    OrderItem(order=orders[3], food_item=fi[4], quantity=1, item_price=fi[4].price),
    OrderItem(order=orders[4], food_item=fi[7], quantity=1, item_price=fi[7].price),
    OrderItem(order=orders[5], food_item=fi[8], quantity=1, item_price=fi[8].price),
    OrderItem(order=orders[5], food_item=fi[9], quantity=2, item_price=fi[9].price),
    OrderItem(order=orders[6], food_item=fi[10], quantity=1, item_price=fi[10].price),
    OrderItem(order=orders[7], food_item=fi[11], quantity=1, item_price=fi[11].price),
    OrderItem(order=orders[8], food_item=fi[5], quantity=1, item_price=fi[5].price),
    OrderItem(order=orders[8], food_item=fi[6], quantity=1, item_price=fi[6].price),
]
OrderItem.objects.bulk_create(order_items)
print(f"✅ Created {len(order_items)} order items")

print("\n🎉 Database populated successfully!")
print(f"   Restaurants : {Restaurant.objects.count()}")
print(f"   Food Items  : {FoodItem.objects.count()}")
print(f"   Customers   : {Customer.objects.count()}")
print(f"   Agents      : {DeliveryAgent.objects.count()}")
print(f"   Orders      : {Order.objects.count()}")
print(f"   Order Items : {OrderItem.objects.count()}")
