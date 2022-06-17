from django.contrib import admin
from employies.models import *

class StaffAdmin(admin.ModelAdmin):
    list_display= ('merchant', 'staff_code', 'staff_name', 'departement')
    list_filter = ('merchant','is_active', 'created_at',)
    search_fields = ('merchant', 'staff_code',  'staff_name',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display= ('merchant', 'departement_code', 'departement_name')
    list_filter = ('is_active', 'created_at',)
    search_fields = ('merchant', 'departement_code',  'departement_name',)


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Staff, StaffAdmin)
