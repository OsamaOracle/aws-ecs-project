from django.db import models


# Create your models here.

class Item(models.Model):
    # id: int
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image_url = models.ImageField(upload_to='pics')
