"""gawaipos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from master.views import get_uom
from microweb.views import *
from django.conf.urls.static import static

admin.site.site_header = 'Gawaipos Admin'
admin.site.site_title = 'Gawaipos Admin'
admin.site.index_title = 'Gawaipos Administration'

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('get/ajax/uom', get_uom, name="get_uom"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)