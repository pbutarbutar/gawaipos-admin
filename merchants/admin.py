from django.contrib import admin
from merchants.models import Merchant,ApiToken,BillingMerchant


class MerchantAdmin(admin.ModelAdmin):
    list_display= ('merchant_number', 'merchant_name', 'merchant_email')
    list_filter = ('is_active', 'created_at',)
    search_fields = ('merchant_number', 'merchant_name',  'merchant_email',)


# Register your models here.
admin.site.register(Merchant, MerchantAdmin)
admin.site.register(ApiToken)
admin.site.register(BillingMerchant)
