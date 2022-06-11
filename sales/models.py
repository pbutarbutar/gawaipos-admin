from lib2to3.pgen2.token import PERCENT
from django.db import models
from django.contrib.auth.models import User
from master.models import Customer, Catalog, Warehouse

# Create your models here.

class Sales(models.Model):
    PERCENT = 'PERCENT'
    AMOUNT = 'AMOUNT'
    
    DISCOUNTYPE = (
        (PERCENT, 'PERCENT'),
        (AMOUNT, 'AMOUNT'),
    )


    trx_num = models.CharField(max_length=50, unique=True)
    trx_date = models.DateField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_customerid')
    voucher_code = models.CharField(max_length=15)
    is_credit = models.BooleanField(default=True)  
    trx_due_date = models.DateField()
    is_ppn = models.BooleanField(default=True)  
    disc_type = models.CharField(max_length=50, choices=DISCOUNTYPE, default=PERCENT)
    disc = models.FloatField(default=0)
    grand_total = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_updatedby')

    def __str__(self):
        return self.trx_num

    class Meta:
        db_table = "sales"


class SalesDetails(models.Model):
    
    sales_id = models.ForeignKey(Sales, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_detail_id')
    item_id = models.ForeignKey(Catalog, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_detail_catalog_id')
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_detail_warehouse_id')
    cogs = models.FloatField(default=0)
    sales_price = models.FloatField(default=0)
    disc_percent = models.FloatField(default=0)
    total = models.FloatField(default=0)  
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_details_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_details_updatedby')

    def __str__(self):
        return self.item_id

    class Meta:
        db_table = "sales_details"