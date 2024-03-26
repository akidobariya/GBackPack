from django.db import models

# Create your models here.


class contactinformation(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.fname
    

class RegisterData1(models.Model):
    username = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    mobilenumber = models.IntegerField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username
    

class ShopProduct(models.Model):
    productname1 = models.CharField(max_length=50)
    productprice1 = models.IntegerField()
    productimage=models.ImageField(upload_to='image/')


    def __str__(self):
        return f"{self.productname1} ---- {self.productprice1}"
    
class cartinfo(models.Model):
    productname1 = models.CharField(max_length=50)
    productprice1 = models.IntegerField()
    productimage=models.ImageField(upload_to='image/')
    producttotal=models.CharField(max_length=10,default=0)
    productquantity=models.CharField(max_length=10,default=0)

    def __str__(self):
        return f"cart product ----> {self.productname1}"
    