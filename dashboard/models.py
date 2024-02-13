from django.db import models

from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    tag_title = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_title

class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    stock_status = models.IntegerField(default=0)
    available_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
