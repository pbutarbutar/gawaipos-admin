from django.contrib import admin
from import_export.admin import ImportExportMixin
from master.models import Warehouse, Catalog, Category,  Supplier, Customer


class WarehouseAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display= ('warehouse_name', 'warehouse_address', 'is_active', 'created_at', 'created_by', 'updated_at', 'updated_by',)

class CategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display= ('catogory_tipe', 'category_name', 'description', 'is_active')

class Catalogdmin(ImportExportMixin, admin.ModelAdmin):
    list_display= ('item_code', 'barcode', 'item_name', 'description', 
                    'category', 'uom', 'is_stock', 'sell_price', 'sell_disc', 
                    'purchase_price', 'purchase_disc', 'is_active', 'created_at', 'updated_at'
                )
    list_filter = ('is_active', 'category', 'uom', 'created_at',)
    search_fields = ('item_code', 'barcode',  'item_name', 'description',)

class Supplierdmin(ImportExportMixin, admin.ModelAdmin):
    list_display= ('supplier_code', 'supplier_name', 'email', 'phone', 'is_active')

class Customerdmin(ImportExportMixin, admin.ModelAdmin):
    list_display= ('customer_code', 'customer_name', 'customer_tipe','email', 'phone', 'is_active')
    list_filter = ('is_active', 'customer_tipe', 'created_at',)
    search_fields = ('customer_code', 'customer_name',  'email', 'phone',)


admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Catalog, Catalogdmin)
admin.site.register(Supplier, Supplierdmin)
admin.site.register(Customer, Customerdmin)