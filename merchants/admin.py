from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from merchants.models import AccountMerchant, Merchant,ApiToken,BillingMerchant


class MerchantAdmin(admin.ModelAdmin):
    list_display= ('merchant_number', 'merchant_name', 'merchant_email')
    list_filter = ('is_active', 'created_at',)
    search_fields = ('merchant_number', 'merchant_name',  'merchant_email',)


class AccountInline(admin.StackedInline):
    model = AccountMerchant
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInline, )

admin.site.register(Merchant, MerchantAdmin)
admin.site.register(ApiToken)
admin.site.register(BillingMerchant)
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
