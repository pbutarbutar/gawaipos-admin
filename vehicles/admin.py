from django.contrib import admin
from vehicles.models import *


admin.site.register(VehicleCategory)
admin.site.register(Vehicle)
admin.site.register(VehicleBrand)
admin.site.register(VehicleBrandOfType)
admin.site.register(VehicleOwner)