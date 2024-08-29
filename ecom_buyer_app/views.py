from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
import random
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Sum
from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
# Create your views here.
def index(request):
    return render(request,"index.html")
otp=0
@csrf_exempt
def signup(request):
    context={}
    if request.method=="POST":
        uname=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_password=request.POST["cpassword"]
        # print(uname,email,password)
        # print(request)
        try:
            Myuser=User.objects.get(email=email)
            context.update({"Message":"User Already exists"})
            return render(request,"register.html",context)
        except:
            if password==confirm_password:  #if check_password(user_password,database_password)
                global otp;
                otp=random.randint(100000,999999)
                subject = 'OTP Verification Code'
                message = f"""Hii Welcome to Ecom World Here is your OTP validated for 1 minutes only 
                otp is {otp}"""
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                send_mail( subject, message, email_from, recipient_list )
                global temp;
                temp={
                    "username":uname,
                    "email":email,
                    "password":password
                }
                return render(request,"otp.html")
            else:
                context.update({"Message":"Password And confirm password Not match"})
                return render(request,"register.html",context)
            context.update({"Message":"Succesfully registered"})
            return render(request,"register.html",context)
    else:
        return render(request,"register.html")

def verify_otp(request):
    context={}
    if request.method=="POST":
        user_otp=request.POST["otp"]
        if otp==int(user_otp):
            User.objects.create(
                username=temp["username"],
                email=temp["email"],
                password=make_password(temp["password"])
            )
            context.update({"Message":"Registration Succesfully"})
            return render(request,"register.html",context)
        else:
            context.update({"Message":"OTP NOT MATCHED"})
            return render(request,"otp.html",context)

    return render(request,"login.html")


def login(request):
    context={}
    if request.method=="POST":
        email=request.POST["email"]
        pwd=request.POST["password"]
        try:
            current_user=User.objects.get(email=email)
            # print(current_user.username)
            # print(current_user.email)
            if check_password(pwd,current_user.password): #hashed
                request.session["user_id"]=current_user.id
                print(request.session)
                return redirect('home')
            else:
                context.update({"Message":"Password Not match"})   
        except:
            context.update({"Message":"User Not Found"})
        return render(request,"login.html",context)
    else:
         return render(request,"login.html")
    
from django.contrib.sites.models import Site
def forgot_password(request):
    context={}
    if request.method=="POST":
        user_email=request.POST["email"]
        domain=Site.objects.get_current()
        # domain=request.get_host()
        try:
            current_user=User.objects.get(email=user_email)
        except:
            context.update({"Message":"User Not Found In our System"})
            return render(request,"forgot-password.html",context)
        print("-------->",domain)
        subject = 'Forgot Password '
        message = f"""
            Here is the link to reset Password
            
            {domain}reset_password/{current_user.id}
            """
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user_email, ]
        send_mail( subject, message, email_from, recipient_list )
    return render(request,"forgot-password.html")


def reset_password(request,pk):
    context={}
    user_detail=User.objects.get(id=pk)
    context.update({"id":user_detail.id})
    if request.method=="POST":
        password =request.POST["pwd"]
        confirm_password=request.POST["cpwd"]
        if password==confirm_password:
            user_detail.password=make_password(password)
            user_detail.save()
            context.update({"Message":"Password Updated Succesfully"})
        else:
            context.update({"Message":"Password and Confirm Password Not match"})
    return render(request,"reset-password.html",context)


def profile(request):
    context={}
    current_user=User.objects.get(id=request.session["user_id"])
    context.update({"user_detail":current_user})
    print(dict(request.POST))
    if request.method=="POST":
        try:
            current_user.Profile_pic=request.FILES["dpimage"]
        except:
            pass
        current_user.username=request.POST["username"]
        if not (request.POST["npassword"]=="" and request.POST["oldpassword"] =="" and request.POST["cnpassword"]==""):
            old_password=request.POST["oldpassword"]
            new_password=request.POST["npassword"]
            confirm_new_password=request.POST["cnpassword"]
            if new_password==confirm_new_password:
                if check_password(old_password,current_user.password):
                    current_user.password=make_password(new_password)
                else:
                    context.update({"Message":"Old Password Not match"})
            else:
                context.update({"Message":"Password And Confirm Password Not match"})
        current_user.save()
        context.update({"Message":"Profile Updated USccesfully"})
        current_user=User.objects.get(id=request.session["user_id"])
        context.update({"user_detail":current_user})
    return render(request,"profile.html",context)

def logout(request):
    del request.session["user_id"]
    # return render(request,"login.html")
    return redirect('login')
from ecom_seller_app.models import *
def home(request):
    context={}
    current_user=User.objects.get(id=request.session["user_id"])
    context.update({"user_detail":current_user})
    all_product=Product.objects.all()
    context.update({"all_product":all_product})
    return render(request,"shop-With-pagination.html",context)
# insert into user values("sugandh","sg@gmail.com",1234)
def product_detail(request,pk):
    my_product=Product.objects.get(id=pk)
    context={}
    current_user=User.objects.get(id=request.session["user_id"])
    context.update({"user_detail":current_user})
    context.update({"my_product":my_product})
    return render(request,"product-with-sidebar.html",context)

def add_to_cart(request,pk):
    current_product=Product.objects.get(id=pk)
    current_user=User.objects.get(id=request.session["user_id"])
    if request.method=="POST":
            quantity=request.POST["quantity"]
    else:
            quantity=1
    try:
        current_cart=Cart.objects.get(product_id=current_product,user_id=current_user)
        current_cart.qunatity+=int(quantity)
        current_cart.save()
        # current_cart.total=current_cart.qunatity*current_product.price
        # current_cart.save()
    except:
        total=quantity*current_product.price
        Cart.objects.create(
            product_id=current_product,
            user_id=current_user,
            qunatity=quantity,
            # total=total
        )
    return redirect('home')
from django.conf import settings

def cart(request):
    context={}
    current_user=User.objects.get(id=request.session["user_id"])
    context.update({"user_detail":current_user})
    current_cart=Cart.objects.filter(user_id=current_user)
    total_amt=current_cart.aggregate(total_sum=Sum('total'))
    print(total_amt)
    # for i in current_cart:
    #     total_amt+=i.total
    context.update({"total_amt":total_amt['total_sum']})
    context.update({"cart_details":current_cart})
    context.update({"razorpay_key":settings.RAZOR_KEY_ID})
    return render(request,"cart.html",context)

import razorpay
client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def checkout(request,val):
    context={}
    if request.method=="POST":
        current_user=User.objects.get(id=request.session["user_id"])
        Myorder=Order.objects.create(
             user_id=current_user,
            final_amount=val,
            address=request.POST["cstreet"],
            city=request.POST["ctown"],
            name=request.POST["cname"],
            lastname=request.POST["clname"],
            email =request.POST["cemail"],
            phone =request.POST["cphone"],
            country=request.POST["ccountry"],
            zipcode=request.POST["czip"],
            state =request.POST["cstate"],
            ordernote=request.POST["cnotes"],
        )
        current_cart=Cart.objects.filter(user_id=current_user)
        for single_cart in current_cart:
            Order_detail.objects.create(
                product_id=single_cart.product_id,
                user_id=current_user,
                qunatity=single_cart.qunatity,
                total=single_cart.total,
                order_id=Myorder
            )
        response=client.payment_link.create({

            "amount": (val)*100,
            "currency": "INR",
            "accept_partial": False,
            "description":Myorder.ordernote,
            "customer": {
                "name": Myorder.name +" " +Myorder.lastname,
                "email":Myorder.email,
                "contact": Myorder.phone
            },
            "notify": {
                "sms": True,
                "email": True
            },
            "reminder_enable": True,
            "notes": {
                "Product Purchase" : Myorder.id
            },
            # "": True,
            "callback_url": "http://127.0.0.1:8000/payment_success/",
            "callback_method": "get"
            
        })
        print("response",response)
        return redirect(response['short_url'])
    else:
        # print("Request get--->",dict(request.GET))
        # amount=request.GET.get("amt")
        context.update({"amount":val})
        return render(request,"checkout.html",context)

def payment_success(request):
    context={}
    current_user=User.objects.get(id=request.session["user_id"])
    context.update({"user_detail":current_user})
    payment_id=request.GET.get("razorpay_payment_id")
    if payment_id:
        print("This is Razorpay Payment_id",request.GET.get("razorpay_payment_id"))
        payment_details=client.payment.fetch(payment_id)
        print("Payment Details--->",payment_details)
        Myorder=Order.objects.get(id=int(payment_details["notes"]["Product Purchase"]))
        print("My order details ",Myorder)
        # Payment.objects.create(

        # )
    return render(request,"payment_success.html",context)

from .forms import UserForm
def check_form(request):
    context={}   
    context.update({"Myform":UserForm}) 
    # context.update({"Myform":User}) 
    # if request.method=="POST":
        # print(request.POST["username"])
        # print(request.POST["email"])
        # print(request.POST["password"])
    return render(request,"check.html",context)
