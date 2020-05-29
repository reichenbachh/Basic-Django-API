from django.db import models

# Create your models here.


class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    description = models.CharField(max_length=500, blank=True)
    createdAt = models.DateField(auto_now_add=True)
