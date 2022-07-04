from email.headerregistry import Address
from django.db import models
from django.contrib.auth.models import User
from merchants.models import Merchant


class VehicleType(models.Model):

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='vehicleType_fk')
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=150)
    year = models.IntegerField()
    color = models.CharField(default='Unknown', max_length=50)
    description = models.TextField(default="")
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_VehicleType_fk')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_VehicleType_fk')
 
    class Meta:
        verbose_name_plural = "Tipes"
        db_table = "vehicle_type"
 
    def __str__(self):
            return f"{self.make} {self.model}"


class VehicleOwner(models.Model):

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='vehicle_owner_merchant_id')
    owner_name = models.CharField(max_length=50)
    owner_hp = models.CharField(max_length=50)
    owner_email = models.CharField(max_length=50)
    id_number = models.CharField(max_length=50)
    address = models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_vehicle_owner_fk')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_vehicle_owner_fk')

    def __str__(self):
        return self.owner_name

    class Meta:
        verbose_name_plural = "Owners"
        db_table = "vehicle_owner"


class Vehicle(models.Model):

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='vehicle_merchant_id')
    vehicletype = models.ForeignKey(VehicleType, on_delete=models.CASCADE, null=True, related_name='vehicle_type_fk')
    vehicle_policy_number = models.CharField(max_length=10, unique=True)
    vehicle_mechine_number = models.CharField(max_length=50,default="")
    current_km = models.IntegerField(default=0)
    vehicle_owner = models.ForeignKey(VehicleOwner, on_delete=models.CASCADE, null=True, related_name='vehicleowner_fk')
    description = models.TextField(default="")
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_vehicle_fk')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_vehicle_fk')

    def __str__(self):
            return f"{self.vehicle_policy_number} {self.vehicle_owner}"

    class Meta:
        verbose_name_plural = "Vehicles"
        db_table = "vehicle"