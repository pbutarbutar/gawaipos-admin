from lib2to3.pgen2.token import PERCENT
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from master.models import Customer, Catalog, Warehouse
from merchants.models import Merchant
from setting_uom.models import Uom

# Create your models here.

class Sales(models.Model):
    PERCENT = 'PERCENT'
    AMOUNT = 'AMOUNT'
    
    DISCOUNTYPE = (
        (PERCENT, 'PERCENT'),
        (AMOUNT, 'AMOUNT'),
    )


    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='sales_merchant_id')
    trx_num = models.CharField(max_length=50, unique=True)
    trx_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_customerid')
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
        verbose_name_plural = "Sales"


class SalesDetails(models.Model):
    
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='sales_item_merchant_id')
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_detail_id')
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_detail_catalog_id')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_detail_warehouse_id')
    cogs = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    uom = models.ForeignKey(Uom, on_delete=models.CASCADE, null=True, related_name='uom_sales_items')
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


class SalesInvoice(models.Model):

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='sales_invoice_merchant_id')
    inv_num = models.CharField(max_length=50, unique=True)
    inv_date = models.DateField()
    inv_due_date = models.DateField()
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_invoice_id')
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_inv_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='sales_inv_updatedby')

    def __str__(self):
        return self.inv_num

    class Meta:
        db_table = "sales_invoice"
        verbose_name_plural = "Invoice"