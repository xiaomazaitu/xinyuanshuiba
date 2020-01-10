from django.contrib import admin

from .models import Order,Product,Order_Product,WaterUser
# Register your models here.
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Order_Product)
admin.site.register(WaterUser)
