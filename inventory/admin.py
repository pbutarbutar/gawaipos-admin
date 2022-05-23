from django.contrib import admin
from inventory.models import StockOnhand


class StockOnhandAdmin(admin.ModelAdmin):
    list_display= ('catalog', 'type_of_item',  'category_of_item', 'warehouse', 'qty', 'uom_of_item', 'sell_price_of_item', 'purchase_price_of_item', 'descriptions', 'updated_at')

    

admin.site.register(StockOnhand, StockOnhandAdmin)