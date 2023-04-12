from django.db import models


class Admin(models.Model):
    Product_id=models.CharField(max_length=5)
    Product_Name=models.CharField(max_lenght=50)
    
class Product_Manager(models.Model):
    Admin=models.foreignkey(Admin, on_delete=models.CASCADE)