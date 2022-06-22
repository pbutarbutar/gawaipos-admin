from django.db import models
from django.contrib.auth.models import User

class Merchant(models.Model):
    GENERAL = 'General'
    AUTOMOTIF = 'Automotif'
    APOTIK = 'Apotik'

    MERCHANT_TYPE = (
        (GENERAL, 'General'),
        (AUTOMOTIF, 'Automotif'),
        (APOTIK, 'Apotik'),
    )

    merchant_number = models.CharField(max_length=50, unique=True)
    merchant_name = models.CharField(max_length=100, default="")
    merchant_type = models.CharField(max_length=50, choices=MERCHANT_TYPE, default=AUTOMOTIF)
    merchant_email = models.CharField(max_length=100, default="")
    merchant_phone = models.CharField(max_length=100, default="")
    merchant_address = models.CharField(max_length=250, default="")
    merchant_owner_name = models.CharField(max_length=100, default="")
    merchant_owner_hp = models.CharField(max_length=100, default="")
    merchant_date = models.DateField()
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_merchant')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_merchant')

    def __str__(self):
        return self.merchant_number


class AccountMerchant(models.Model): 

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_account_merchant_id')
    role_user = models.CharField(
        max_length=8,
        default='Merchant',
        choices=[('GAWAIPOS', 'Gawaipos'), ('MERCHANT', 'Merchant')]
    )
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, default='null', related_name='account_merchant_id')
    name = models.CharField(max_length=25, default="")
    birthday = models.DateTimeField()
    gender = models.CharField(
        max_length=6,
        choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')]
    )
    def __str__(self):
        return self.user.username
    class Meta:
        db_table = "account_merchants"

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