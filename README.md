# 🍔 FoodORM - Django ORM Web Application
### Food Delivery Platform (Zomato/Swiggy style) | Ex 01

---

## 📋 Project Overview
A Django web application managing an online food delivery platform using **Object Relational Mapping (ORM)**.

### Database Tables (6 models)
| Table | Primary Key | Fields |
|-------|-------------|--------|
| `food_restaurants` | `restaurant_id` | name, location, cuisine_type, rating, is_active, created_at |
| `food_items` | `item_id` | restaurant(FK), item_name, description, price, category, is_veg, is_available |
| `food_customers` | `customer_id` | full_name, email, phone, address, city, joined_date |
| `food_delivery_agents` | `agent_id` | agent_name, phone, vehicle_type, status, rating |
| `food_orders` | `order_id` | customer(FK), restaurant(FK), delivery_agent(FK), order_status, total_amount, delivery_address, order_date, estimated_delivery |
| `food_order_items` | `orderitem_id` | order(FK), food_item(FK), quantity, item_price |

---

## 🚀 Setup & Run (Step-by-Step)

### Step 1 – Clone / Navigate to project folder
```bash
cd foodorm
```

### Step 2 – Create & activate virtual environment
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### Step 3 – Install Django
```bash
pip install -r requirements.txt
```

### Step 4 – Run migrations (creates SQLite database)
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5 – Populate database with 10+ sample records
```bash
python populate_data.py
```

### Step 6 – Create superuser (for Admin panel)
```bash
python manage.py createsuperuser
# Enter: username, email, password
```

### Step 7 – Start development server
```bash
python manage.py runserver
```

### Step 8 – Open in browser
| URL | Page |
|-----|------|
| http://127.0.0.1:8000/ | Dashboard |
| http://127.0.0.1:8000/restaurants/ | All Restaurants |
| http://127.0.0.1:8000/orders/ | All Orders |
| http://127.0.0.1:8000/customers/ | All Customers |
| http://127.0.0.1:8000/agents/ | Delivery Agents |
| http://127.0.0.1:8000/admin/ | Admin Panel |

---

## 📁 Project Structure
```
foodorm/
├── manage.py
├── requirements.txt
├── populate_data.py        ← Run this to add sample data
├── foodorm/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── fooddelivery/
│   ├── models.py           ← ORM Models (6 tables)
│   ├── views.py
│   ├── urls.py
│   └── admin.py
└── templates/
    └── fooddelivery/
        ├── base.html
        ├── dashboard.html
        ├── restaurant_list.html
        ├── restaurant_detail.html
        ├── order_list.html
        ├── order_detail.html
        ├── customer_list.html
        └── agent_list.html
```

---

## 🔑 Key ORM Concepts Used
- `models.AutoField` – Primary keys
- `models.ForeignKey` – Relationships (Order → Customer, Restaurant, Agent)
- `models.CharField`, `DecimalField`, `BooleanField`, `DateTimeField` – Field types
- `objects.all()`, `objects.filter()`, `objects.count()` – QuerySets
- `select_related()` – Optimized JOIN queries
- `bulk_create()` – Efficient batch inserts
- `on_delete=CASCADE` / `SET_NULL` – Referential integrity
