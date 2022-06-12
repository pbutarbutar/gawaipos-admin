from django.contrib import admin
from .models import Profile, AboutUs, ProductList, ProductListImages
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.models import Attachment


class AboutUsAdmin(SummernoteModelAdmin):

    list_display = ('slug', 'title', 'body', 'description', 'is_draft', 'created_by', 'created_at')
    list_filter = ('is_draft', 'created_at')
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
    
class ProductListAdmin(SummernoteModelAdmin):

    list_display = ('slug', 'product_title', 'product_description', 'product_view_body', 'is_draft', 'created_by', 'created_at')
    list_filter = ('is_draft', 'created_at')
    search_fields = ('product_title', )
    summerenote_fields =('product_view_body',)

class ProductListImagesAdmin(SummernoteModelAdmin):

    list_display = ('product_list_id','slug', 'product_images_title', 'product_images_body', 'product_images',  'is_draft', 'created_by', 'created_at')
    list_filter = ('is_draft', 'created_at')
    search_fields = ('product_title', )
    summerenote_fields =('product_images_body',)

admin.site.register(Profile)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(ProductList, ProductListAdmin)
admin.site.register(ProductListImages, ProductListImagesAdmin)

admin.site.unregister(Attachment)