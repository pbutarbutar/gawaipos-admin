from django.contrib import admin

from master.models import Warehouse, Catalog, Category, Uom


class WarehouseAdmin(admin.ModelAdmin):

    list_display= ('warehouse_name', 'warehouse_address', 'is_active', 'created_at', 'created_by', 'updated_at', 'updated_by',)

class CategoryAdmin(admin.ModelAdmin):
    list_display= ('catogory_tipe', 'category_name', 'description', 'is_active')

class UomAdmin(admin.ModelAdmin):
    list_display= ('uom_name', 'description', 'is_active')

class Catalogdmin(admin.ModelAdmin):
    list_display= ('item_code', 'barcode', 'item_name', 'description', 
                    'category', 'uom', 'is_stock', 'sell_price', 'sell_disc', 
                    'purchase_price', 'purchase_disc', 'is_active', 'created_at', 'updated_at'
                )

admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Uom, UomAdmin)
admin.site.register(Catalog, Catalogdmin)