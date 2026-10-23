from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    min_desc = models.TextField(max_length=150)
    desc = models.TextField(max_length=500)
    price = models.IntegerField(max_length=9)
    image = models.FileField(upload_to='products_images')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"