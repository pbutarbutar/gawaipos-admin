from tabnanny import verbose
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from setting_uom.models import Uom

# Create your models here.

class Warehouse(models.Model):

    warehouse_name = models.CharField(max_length=50, unique=True)
    warehouse_address = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_wh')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_wh')

    def __str__(self):
        return self.warehouse_name

class Category(models.Model):
    PART = 'Part'
    SERVICE = 'Service'
    CONSUMABLE = 'Consumable'
    OLI = 'Oli'
    FOOD = 'Food'
    ANOTHER = 'Another'

    ITEMTYPE = (
        (PART, 'Part'),
        (SERVICE, 'Service'),
        (CONSUMABLE, 'Consumable'),
        (OLI, 'OLI'),
        (FOOD, 'FOOD'),
        (ANOTHER, 'Another'),
    )

    catogory_tipe = models.CharField(max_length=50, choices=ITEMTYPE, default=PART)
    category_name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_ctg')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_ctg')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'

class Catalog(models.Model):

    item_code = models.CharField(max_length=50, unique=True)
    barcode = models.CharField(max_length=50)
    item_name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    uom = models.ForeignKey(Uom, on_delete=models.CASCADE, related_name='uom_catalog_id')
    sell_price = models.IntegerField() 
    sell_disc = models.IntegerField()
    purchase_price = models.IntegerField() 
    purchase_disc = models.IntegerField()
    is_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_ctlg')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_ctlg')

    def __str__(self):
        return self.item_name


class Supplier(models.Model):

    supplier_code = models.CharField(max_length=50, unique=True)
    supplier_name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.supplier_name

class Customer(models.Model):
    CASH = 'Cash'
    CREDIT = 'Credit'

    CUSTTYPE = (
        (CASH, 'Cash'),
        (CREDIT, 'Credit'),
    )

    customer_tipe = models.CharField(max_length=50, choices=CUSTTYPE, default=CASH)
    customer_code = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.customer_name

