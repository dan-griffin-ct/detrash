from django.db import models

class AppUser(models.Model):
    email = models.CharField(max_length=256, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.email 