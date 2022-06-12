from django.db import models
from django.contrib.auth.models import User
from merchants.models import Merchant

class VehicleCategory(models.Model):
    
    name_category = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_vehicle_category_fk')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_vehicle_category_fk')

    def __str__(self):
        return self.name_category


class VehicleBrand(models.Model):

    brand = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_vehicle_brand_fk')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_vehicle_brand_fk')

    def __str__(self):
        return self.brand

class VehicleBrandOfType(models.Model):

    name_type = models.CharField(max_length=50)
    brand_id = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_vehicle_brand_type_fk')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_vehicle_brand_type_fk')

    def __str__(self):
        return self.brand

class Vehicle(models.Model):

    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='vehicle_merchant_id')
    vehicle_number = models.CharField(max_length=50, unique=True)
    vehicle_date = models.DateField()
    vehicle_category_id = models.ForeignKey(VehicleCategory, on_delete=models.CASCADE,  null=True, related_name='vehicle_category_id_fk')
    brand_id = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE, null=True, related_name='vehicle_brand_id_fk')
    brand_type_id = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE, null=True, related_name='vehicle_type_fk')
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_vehicle_fk')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_vehicle_fk')

    def __str__(self):
        return self.vehicle_number

class VehicleOwner(models.Model):

    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='vehicle_owner_merchant_id')
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle_id_owner_fk')
    owner_name = models.CharField(max_length=50)
    owner_hp = models.CharField(max_length=50)
    owner_email = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_vehicle_owner_fk')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_vehicle_owner_fk')

    def __str__(self):
        return self.brand