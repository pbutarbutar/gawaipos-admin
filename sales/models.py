from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sales(models.Model):

    no_trx = models.CharField(max_length=50, unique=True)
    date_trx = models.CharField(max_length=50)
    total = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='swh')
    #updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='swh')

    def __str__(self):
        return self.no_trx
