from django.contrib import admin
from import_export.admin import ImportExportMixin
from setting_uom.models import Uom, GroupUom, GroupUomDefinition


class UomAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display= ('uom_name', 'description', 'is_active')


admin.site.register(Uom, UomAdmin)
admin.site.register(GroupUom)
admin.site.register(GroupUomDefinition)
