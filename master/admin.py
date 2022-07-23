from django.contrib import admin
from import_export.admin import ImportExportMixin
from master.models import Warehouse, Catalog, Supplier, Customer


class WarehouseAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'merchant', 'warehouse_name', 'warehouse_address', 'is_active', 'created_at', 'created_by', 'updated_at',
        'updated_by',)


class CatalogAdmin(ImportExportMixin, admin.ModelAdmin):

    change_form_template = 'master/catalog_form.html'

    list_display = ('merchant', 'item_code', 'barcode', 'item_name', 'description',
                    'classification', 'uom_inventory', 'is_stock', 'uom_group', 'uom_sales', 'uom_sell_price',
                    'sell_price', 'sell_disc',
                    'uom_purchase', 'uom_purchase_price', 'purchase_price', 'purchase_disc', 'is_active', 'created_at',
                    'updated_at'
                    )
    list_filter = ('is_active', 'classification', 'uom_inventory', 'created_at',)

    search_fields = ('item_code', 'barcode', 'item_name', 'description',)


class SupplierAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('merchant', 'supplier_code', 'supplier_name', 'email', 'phone', 'is_active')


class CustomerAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('merchant', 'customer_code', 'customer_name', 'customer_tipe', 'email', 'phone', 'is_active')
    list_filter = ('is_active', 'customer_tipe', 'created_at',)
    search_fields = ('customer_code', 'customer_name', 'email', 'phone',)


def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

    for app in app_list:
        if app['app_label'] == 'auth':
            ordering = {
                'Warehouse': 1,
                'Master Item': 2,
                'Supplier': 3,
                'Customer': 4,
            }

    return app_list


admin.AdminSite.get_app_list = get_app_list

admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Customer, CustomerAdmin)
