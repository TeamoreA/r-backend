from django.db import models
from utils.base_model import MyBaseModel
from django.contrib.auth.models import User

# Create your models here.

class Category(MyBaseModel):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name
    


class Product(MyBaseModel):
    name = models.CharField(max_length=60)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=50)
    size = models.FloatField(null=True)
    price = models.FloatField(default=0)
    no_of_items = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    product_images = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name
    
