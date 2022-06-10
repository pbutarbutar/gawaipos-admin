from django.contrib import admin
from import_export.admin import ImportExportMixin
from sales.models import Sales


class SalesAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display= ('no_trx', 'date_trx', 'total',  'is_active')


admin.site.register(Sales, SalesAdmin)