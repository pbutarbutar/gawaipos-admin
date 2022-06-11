from django.contrib import admin
from import_export.admin import ImportExportMixin
from sales.models import Sales


class SalesAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display= ('trx_num', 'trx_date', 'customer_id', 'is_credit', 'trx_due_date', 'voucher_code', 'is_ppn', 'disc_type', 'disc', 'grand_total', 'created_by', 'created_at',)


admin.site.register(Sales, SalesAdmin)