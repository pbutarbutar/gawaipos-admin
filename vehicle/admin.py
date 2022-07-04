from django.contrib import admin
from vehicle.models import *

class VehicleTypeAdmin(admin.ModelAdmin):
    list_display= ('merchant', 'make', 'model', 'year', 'color', 'description',  'is_active', 'created_at', 'created_by')
    list_filter = ('merchant','model', 'year', 'color', 'is_active', 'created_at',)
    search_fields = ('merchant', 'make', 'description')

class VehicleAdmin(admin.ModelAdmin):
    list_display= ('merchant', 'vehicletype', 'vehicle_policy_number', 'vehicle_mechine_number', 'current_km', 'vehicle_owner', 'description',  'is_active', 'created_at', 'created_by')
    list_filter = ('merchant','vehicletype', 'current_km', 'is_active', 'created_at',)
    search_fields = ('merchant', 'vehicle_policy_number', 'vehicle_mechine_number', 'description', )

class VehicleOwnerAdmin(admin.ModelAdmin):
    list_display= ('merchant', 'owner_name', 'owner_email', 'id_number', 'address', 'is_active', 'created_at', 'created_by')
    list_filter = ('merchant', 'is_active', 'created_at',)
    search_fields = ('merchant', 'owner_name', 'owner_email', 'id_number', 'address', )

def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

    for app in app_list:
        if app['app_label'] == 'auth':
            ordering = {
                'Tipes': 1,
                'Owners': 2,
                'Vehicles': 3,
            }
            
    return app_list

admin.AdminSite.get_app_list = get_app_list

admin.site.register(VehicleType, VehicleTypeAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleOwner, VehicleOwnerAdmin)