from django.db import models
from categories.models import Category

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category, related_name="items")


    def __str__(self):
        return self.name
