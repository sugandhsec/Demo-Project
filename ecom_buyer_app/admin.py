from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Order_detail)
admin.site.register(Payment)
# admin.site.register()