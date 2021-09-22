from django.db import models
from core import models as core_models
from Users import models as user_models
from Products import models as product_models




class Cart(core_models.TimeStampedModel):
    
    product = models.ForeignKey("Products.product",  related_name = "Cart", on_delete = models.CASCADE, null=True)
    user = models.ForeignKey("Users.user",  related_name = "Cart", on_delete = models.CASCADE, null=True)
    product_inventory = models.ForeignKey("Products.product_inventory", related_name= "Cart", on_delete = models.CASCADE, null=True)
    quantity = models.IntegerField()



