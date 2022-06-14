from django.db import models
from django.contrib.auth.models import User
from djmoney.money import Money
from master.models import Catalog, Warehouse
from merchants.models import Merchant

class StockOnhand(models.Model):

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='inv_merchant_id')
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, blank=False, null=False, related_name='catalog_inv')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, blank=False, null=False, related_name='warehouse_inv')
    descriptions = models.CharField(max_length=50)
    qty = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_inv')

    def __str__(self):
        return self.catalog.item_name

    def name_of_item(self):
        return self.catalog.item_name

    def uom_of_item(self):
        return self.catalog.uom

    def type_of_item(self):
        return self.catalog.category.catogory_tipe
    
    def category_of_item(self):
        return self.catalog.category

    def sell_price_of_item(self):
        return Money(self.catalog.sell_price, 'IDR')

    def purchase_price_of_item(self):
        return Money(self.catalog.purchase_price, 'IDR')