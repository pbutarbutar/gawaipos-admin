from django.db import models
from django.contrib.auth.models import User
from merchants.models import Merchant

class Department(models.Model):

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='dept_merchant_id')
    departement_code = models.CharField(max_length=50, unique=True)
    departement_name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_dept')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_dept')

    def __str__(self):
        return self.departement_name


class Staff(models.Model):

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='staff_merchant_id')
    staff_code = models.CharField(max_length=50, unique=True)
    staff_name = models.CharField(max_length=100, default="")
    departement = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, related_name='staff_departement_id')
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_staff')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_staff')

    def __str__(self):
        return self.staff_name

