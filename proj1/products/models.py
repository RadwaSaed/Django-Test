from django.db import models

# Create your models here.
class Products(models.Model):
    Name = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)