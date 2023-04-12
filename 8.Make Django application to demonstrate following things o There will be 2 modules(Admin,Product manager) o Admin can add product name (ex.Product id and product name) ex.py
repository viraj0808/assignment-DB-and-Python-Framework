from django.db import models


class Product_manager(models.Model): 
    product_id = models.AutoField(primary_key=True) 
    product_name = models.CharField(max_length=60)

def __str__(self):
    return self.product_name

class ProductSubCat(models.Model): 
    product = models.ForeignKey(Product_manager, on_delete=models.CASCADE) 
    product_price = models.DecimalField(max_digits=12, decimal_places=3) 
    product_image = models.ImageField(upload_to='images/') 
    product_model = models.CharField(max_length=60) 
    product_ram = models.CharField(max_length=60)

def __str__(self):
    return self.product.product_name