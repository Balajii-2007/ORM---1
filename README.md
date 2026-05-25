# Ex01 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
~~~
from django.db import models

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    UserID = models.IntegerField()
    OrderDate = models.DateField()
    ItemName = models.CharField(max_length=255)
    OrderQty = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    DeliveryAddress = models.TextField()

    def str(self):
        return f"Order {self.OrderID} - {self.ItemName}"
from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('OrderID', 'ItemName', 'OrderQty', 'TotalAmount')

admin.site.register(Order, OrderAdmin)
~~~



## OUTPUT

<img width="1229" height="614" alt="image" src="https://github.com/user-attachments/assets/008910b8-57d9-4686-8558-3207289d3079" />


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
