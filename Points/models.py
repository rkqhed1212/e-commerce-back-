from django.db import models
from core import models as core_models
from Users import models as user_models
from Products import models as product_models
from django.utils.html import mark_safe



class Points(core_models.TimeStampedModel):
    
    product = models.ForeignKey("Products.product",  related_name = "Points", on_delete = models.CASCADE, null=True)
    user = models.ForeignKey("Users.user",  related_name = "Points", on_delete = models.CASCADE, null=True)
    content = models.CharField(max_length=10, null = True)
    amount = models.IntegerField()
    point_status = models.CharField(max_length=10)