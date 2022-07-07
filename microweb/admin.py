from tkinter import Menu
from django.contrib import admin
from .models import Profile, AboutUs, ProductList, ProductListImages
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.models import Attachment
from merchants.models import AccountMerchant, Merchant


class AboutUsAdmin(SummernoteModelAdmin):

    llist_display = ('merchant', 'slug', 'title', 'body', 'description', 'is_draft', 'created_by', 'created_at')
    list_filter = ('is_draft', 'created_at', 'merchant')
    search_fields = ('title', )
    fieldset = (
        (None, {
            'fields':(('title', 'slug'), 'body'),
        }),
        ("Advanced Options", {
            'fields': ('is_draft', ),
            'description':'Option to Configure'
        })
    )
    summerenote_fields =('body',)

    def get_queryset(self, request):

        # Override the get_queryset method for Admin
        qs = super(AboutUsAdmin, self).get_queryset(request)
        
        merchant_acc = AccountMerchant.objects.filter(user_id=request.user).first()
        print("debug :", merchant_acc.role_user)

        if merchant_acc.role_user == "GAWAIPOS": 
            return qs

        #if request.user.is_superuser:
          #  return qs
        return qs.filter(merchant = merchant_acc.merchant)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "merchant":
            merchant_acc = AccountMerchant.objects.filter(user_id=request.user).first()
            print("debug :", merchant_acc.merchant_id)

            if merchant_acc.role_user != "GAWAIPOS": 
                kwargs['queryset'] = Merchant.objects.filter(id=merchant_acc.merchant_id)

        return super(AboutUsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    
class ProductListAdmin(SummernoteModelAdmin):

    list_display = ('merchant', 'slug', 'product_title', 'product_description', 'product_view_body', 'is_draft', 'created_by', 'created_at')
    list_filter = ('is_draft', 'created_at', 'merchant')
    search_fields = ('product_title', )
    summerenote_fields =('product_view_body',)

    def get_queryset(self, request):

        # Override the get_queryset method for Admin
        qs = super(ProductListAdmin, self).get_queryset(request)
        
        merchant_acc = AccountMerchant.objects.filter(user_id=request.user).first()
        print("debug :", merchant_acc.role_user)

        if merchant_acc.role_user == "GAWAIPOS": 
            return qs

        #if request.user.is_superuser:
          #  return qs
        return qs.filter(merchant = merchant_acc.merchant)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "merchant":
            merchant_acc = AccountMerchant.objects.filter(user_id=request.user).first()
            print("debug :", merchant_acc.merchant_id)

            if merchant_acc.role_user != "GAWAIPOS": 
                kwargs['queryset'] = Merchant.objects.filter(id=merchant_acc.merchant_id)

        return super(ProductListAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class ProductListImagesAdmin(SummernoteModelAdmin):

    list_display = ('merchant', 'product_category','slug', 'product_images_title', 'product_images_body', 'product_images',  'is_draft', 'created_by', 'created_at')
    list_filter = ('is_draft', 'created_at', 'merchant_id')
    search_fields = ('product_title', )
    summerenote_fields =('product_images_body',)

    def get_queryset(self, request):

        # Override the get_queryset method for Admin
        qs = super(ProductListImagesAdmin, self).get_queryset(request)
        
        merchant_acc = AccountMerchant.objects.filter(user_id=request.user).first()
        print("debug :", merchant_acc.role_user)

        if merchant_acc.role_user == "GAWAIPOS": 
            return qs

        #if request.user.is_superuser:
          #  return qs
        return qs.filter(merchant = merchant_acc.merchant)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "merchant":
            merchant_acc = AccountMerchant.objects.filter(user_id=request.user).first()
            print("debug :", merchant_acc.merchant_id)

            if merchant_acc.role_user != "GAWAIPOS": 
                kwargs['queryset'] = Merchant.objects.filter(id=merchant_acc.merchant_id)

        return super(ProductListImagesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class ProfileAdmin(SummernoteModelAdmin):
    list_display = ('merchant', 'slug', 'title', 'name_business', 'is_active', 'created_by', 'created_at')
    list_filter = ('is_active', 'created_at', 'merchant')
    search_fields = ('title', 'slug', 'name_business')
    summerenote_fields =('home_description',)
    
    
    def get_queryset(self, request):

        # Override the get_queryset method for Admin
        qs = super(ProfileAdmin, self).get_queryset(request)
        
        merchant_acc = AccountMerchant.objects.filter(user_id=request.user).first()
        print("debug :", merchant_acc.role_user)

        if merchant_acc.role_user == "GAWAIPOS": 
            return qs

        #if request.user.is_superuser:
          #  return qs
        return qs.filter(merchant = merchant_acc.merchant)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "merchant":
            merchant_acc = AccountMerchant.objects.filter(user_id=request.user).first()
            print("debug :", merchant_acc.merchant_id)

            if merchant_acc.role_user != "GAWAIPOS": 
                kwargs['queryset'] = Merchant.objects.filter(id=merchant_acc.merchant_id)

        return super(ProfileAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(ProductList, ProductListAdmin)
admin.site.register(ProductListImages, ProductListImagesAdmin)

admin.site.unregister(Attachment)