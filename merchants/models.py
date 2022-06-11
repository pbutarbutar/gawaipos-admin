from django.db import models
from django.contrib.auth.models import User

class Merchant(models.Model):

    merchant_number = models.CharField(max_length=50, unique=True)
    merchant_date = models.DateField()
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_merchant')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_merchant')

    def __str__(self):
        return self.merchant_number

class ApiToken(models.Model):

    token_api_internal = models.CharField(max_length=250, unique=True)
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_merchant_token_api')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_merchant_token_api')

    def __str__(self):
        return self.token_api_internal

class BillingMerchant(models.Model):

    bill_desc = models.CharField(max_length=250, unique=True)
    bill_date = models.DateField()
    bill_due_date = models.DateField()
    bill_amount = models.FloatField(default=0)
    bill_paid = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_merchant_billing')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_merchant_billing')

    def __str__(self):
        return self.token_api_internal