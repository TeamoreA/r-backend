from django.db import models
from utils.base_model import MyBaseModel

# Create your models here.

class Category(MyBaseModel):
    name = models.CharField(max_length=100)


class Product(MyBaseModel):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=50)
    size = models.FloatField(blank=True)
    image = models.ImageField(upload_to='images')
