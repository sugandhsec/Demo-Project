from django.db import models
from ecom_seller_app.models import *
# Create your models here.

# table creation code
class User(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password =models.CharField(max_length=100)
    Profile_pic =models.FileField(upload_to="buyer_user_image/",default="Anonymous.jpg")

    def __str__(self):
        return self.username + " , "+self.email
# create table user(
#     username varchar(20), pk
#     email varchar(20),
#     password varchar(20), Django Forms  ,DJango Model Forms
# )


class Cart(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    qunatity=models.IntegerField(default=1)
    total=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Calculate the total by multiplying the quantity with the product's price
        self.total = self.qunatity * self.product_id.price
        # Call the original save method to save the instance
        super(Cart, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.product_id.name 


class Order(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    final_amount=models.IntegerField(default=0)
    address=models.TextField(max_length=500)
    city=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email =models.EmailField()
    phone =models.CharField(max_length=100)
    country=models.CharField(max_length=40)
    zipcode=models.CharField(max_length=40)
    state =models.CharField(max_length=40)
    ordernote =models.TextField()

    def __str__(self):
        return str(self.id)
    
class Order_detail(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    qunatity=models.IntegerField(default=1)
    total=models.IntegerField(default=0)
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.total)
    
class Payment(models.Model):
    choice=(
        # (visible to us,saved in database)
        ("Success","Success"),
        ("Fail","Fail"),
    )
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
    Amount=models.IntegerField(default=0)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    payment_status=models.CharField(max_length=20,choices=choice,blank=True,null=True)
    transaction_id=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now=True)
    methods=models.CharField(max_length=40)

    def __str__(self):
        return self.transaction_id



