from django.db import models


# # Create your models here.
class Seller_User(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password =models.CharField(max_length=100)
    profile_picture=models.FileField(upload_to="seller_user_images/",default="anonymous.jpg")

    def __str__(self):
        return self.username + " , "+self.email
    
class Product(models.Model):
    name =models.CharField(max_length=100)
    image =models.FileField(upload_to="product_images/",blank=True,default="def_pro.jpg")
    price =models.IntegerField()
    description =models.TextField()
    quantity =models.IntegerField()
    seller_user=models.ForeignKey(Seller_User,on_delete=models.DO_NOTHING)
    # slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.name
    

