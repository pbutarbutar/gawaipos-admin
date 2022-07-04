from cProfile import label
from django.contrib import admin
from import_export.admin import ImportExportMixin
from sales.models import Sales, SalesInvoice, SalesDetails


class SalesDetailsInline(admin.TabularInline):
    model = SalesDetails
    fields = ('sales', 'catalog', 'warehouse', 'qty', 'uom', 'sales_price', 'disc_percent', 'total')
    extra = 3


class SalesAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display= ('trx_num', 'trx_date', 'customer', 'is_credit', 'trx_due_date', 'voucher_code', 'is_ppn', 'disc_type', 'disc', 'grand_total', 'created_by', 'created_at',)
    list_filter = ('trx_num','is_credit', 'trx_date', 'created_at',)
    search_fields = ('trx_num', 'customer', 'trx_date')

    inlines = [SalesDetailsInline, ]

class SalesInvoiceAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display= ('inv_num', 'inv_date', 'sales', 'inv_due_date', 'created_by', 'created_at',)
    list_filter = ('inv_num','inv_date', 'inv_due_date', 'created_at',)
    search_fields = ('inv_num', 'inv_date', 'sales')


def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

    for app in app_list:
        if app['app_label'] == 'auth':
            ordering = {
                'Sales': 1,
                'Invoice': 2
            }
            
    return app_list

admin.AdminSite.get_app_list = get_app_list

admin.site.register(Sales, SalesAdmin)
admin.site.register(SalesInvoice, SalesInvoiceAdmin)