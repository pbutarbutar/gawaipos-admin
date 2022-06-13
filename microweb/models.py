from django.db import models
from django.contrib.auth.models import User
from merchants.models import Merchant

class Profile(models.Model):
    
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True)
    slug = models.CharField(max_length=100)
    keywords = models.CharField(max_length=150, default="")
    title = models.CharField(max_length=100)
    name_business = models.CharField(max_length=50)
    address_business = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    wa_number = models.CharField(max_length=15)
    email = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='logo')
    slogan = models.CharField(max_length=150)
    facebook_link = models.CharField(max_length=150, default="")
    twitter_link = models.CharField(max_length=150, default="")
    linked_link = models.CharField(max_length=150, default="")
    youtube_link = models.CharField(max_length=150, default="")
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
    
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=100)
    keywords = models.CharField(max_length=150, default="")
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


class ProductList(models.Model):
    
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True)
    slug = models.CharField(max_length=100)
    product_keywords = models.CharField(max_length=150, default="")
    product_title = models.CharField(max_length=100)
    product_description= models.CharField(max_length=250)
    product_view_body= models.TextField()
    wa_number = models.CharField(max_length=15)
    thumb_product = models.ImageField(upload_to='thumb_product')
    is_draft = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_mcrw_products')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_mcrw_products')
    
    def __str__(self):
        return self.product_title

    class Meta:
        db_table = "microweb_product_list"

class ProductListImages(models.Model):
    
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True)
    slug = models.CharField(max_length=100)
    product_images_keywords = models.CharField(max_length=150, default="")
    product_images_title = models.CharField(max_length=100, default="")
    product_images_body= models.TextField()
    product_list_id = models.ForeignKey(ProductList, on_delete=models.CASCADE, related_name='product_list_images_id')
    product_images = models.ImageField(upload_to='product_images')
    is_draft = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_mcrw_images')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_mcrw_images')
    
    def __str__(self):
        return self.product_images_title

    class Meta:
        db_table = "microweb_product_list_images"
