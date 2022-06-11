from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    slug = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    name_business = models.CharField(max_length=50)
    address_business = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    wa_number = models.CharField(max_length=15)
    email = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='logo')
    slogan = models.CharField(max_length=150)
    google_tag_manager_id = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_mcrw')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_mcrw')
    
    def __str__(self):
        return self.name_business

    class Meta:
        db_table = "microweb_profifile"

class AboutUs(models.Model):
    
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    description = models.CharField(max_length=250)
    is_draft = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_mcrw_aboutus')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_mcrw_aboutus')
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "microweb_about_us"


