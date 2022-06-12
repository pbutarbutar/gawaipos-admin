from django.db import models
from django.contrib.auth.models import User
from merchants.models import Merchant

class GroupUom(models.Model):

    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='uom_group_merchant_id')
    group_uom = models.CharField(max_length=10, unique=True, blank=False, default='')
    description = models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='group_oum_user_created')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='group_oum_user_update')

    def __str__(self):
        return self.group_uom


class Uom(models.Model):

    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='uom_merchant_id')
    uom_code = models.CharField(max_length=10, unique=True, blank=False, default='')
    uom_name = models.CharField(max_length=20, default="")
    uom_length = models.CharField(max_length=20, default="")
    uom_width = models.CharField(max_length=20, default="")
    uom_height = models.CharField(max_length=20, default="")
    uom_volume = models.CharField(max_length=20, default="")
    uom_volume_uom = models.CharField(max_length=20, default="")
    uom_weight = models.CharField(max_length=20, default="")
    description = models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_oum')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_oum')

    def __str__(self):
        return self.uom_name


class GroupUomDefinition(models.Model):

    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='uom_group_def_merchant_id')
    group_id = models.ForeignKey(GroupUom, on_delete=models.CASCADE, related_name='group_id_definition')
    qty_to = models.FloatField(default=0)
    uom_to = models.ForeignKey(Uom, on_delete=models.CASCADE, related_name='uom_definition_to')
    base_qty = models.FloatField(default=0)
    base_uom = models.ForeignKey(Uom, on_delete=models.CASCADE, related_name='uom_definition_base')
    description = models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='group_definition_oum_user_created')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='group_definition_oum_user_update')

    def __str__(self):
        return self.description