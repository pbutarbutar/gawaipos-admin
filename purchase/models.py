from django.db import models
from django.contrib.auth.models import User
from merchants.models import Merchant

class Purchase(models.Model):

    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='purchase_merchant_id')
    purchase_number = models.CharField(max_length=50, unique=True)
    purchase_date = models.DateField()
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_purchase')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_purchase')

    def __str__(self):
        return self.purchase_number

