from django.contrib import admin
from merchants.models import Merchant,ApiToken,BillingMerchant

# Register your models here.
admin.site.register(Merchant)
admin.site.register(ApiToken)
admin.site.register(BillingMerchant)
