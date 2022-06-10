from django.contrib import admin
from locations.models import Country,State,City,Street

# Register your models here.

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Street)