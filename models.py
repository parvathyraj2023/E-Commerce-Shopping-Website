from django.db import models

# Create your models here.
class categorydb(models.Model):
    Category_name = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    Category_image = models.ImageField(upload_to="Profile", null=True, blank=True)

class productdb(models.Model):
    Category = models.CharField(max_length=50, null=True, blank=True)
    Product_name = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Category_image = models.ImageField(upload_to="Profile", null=True, blank=True)
