from django.db import models

# Create your models here.

""""
Product
-Nom
-Prix
-La quantité en stock
-Description
-Image
"""

class Product(models.Model):
    nom=models.CharField(max_length=130)
    prix=models.FloatField(default=0.0)
    quantity_stock=models.IntegerField(default=0)
    description=models.TextField(blank=True)
    thumbnail=models.ImageField(upload_to="products", blank=True, null=True)
