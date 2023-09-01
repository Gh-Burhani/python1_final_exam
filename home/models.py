from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    pub_data = models.DateField()
    author =models.CharField(null=True, max_length=250)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=999)
    
    
    
