from django.db import models
from core import models as core_models
from Users import models as user_models
from Products import models as product_models



class Group_order(core_models.TimeStampedModel):
    
    user = models.ForeignKey("Users.user", related_name = "Group_order", on_delete = models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    pcc = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.pk)



class Product_order(core_models.TimeStampedModel):

    order_number = models.ForeignKey("Group_order", related_name = "Product_order", on_delete = models.CASCADE , null=True, blank=True)
    product = models.ForeignKey("Products.product", related_name = "Product_order", on_delete = models.CASCADE , null=True, blank=True)
    color = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
