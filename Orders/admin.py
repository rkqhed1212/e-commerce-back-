from django.contrib import admin
from . import models



@admin.register(models.Group_order)
class Group_order(admin.ModelAdmin):
    
    list_display = (
        "pk",
        "user",
        "status",
        "address",
    )


@admin.register(models.Product_order)
class Product_orderAdmin(admin.ModelAdmin):
    
    list_display = (
        "product",
        "color",
        "size",
        "quantity",
        "price",
    )


