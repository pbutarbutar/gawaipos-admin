from django.contrib import admin
from .models import Profile, AboutUs
from django_summernote.admin import SummernoteModelAdmin


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
    



admin.site.register(Profile)
admin.site.register(AboutUs, AboutUsAdmin)
