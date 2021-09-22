from django.db import models
from core import models as core_models
from Users import models as user_models
from Products import models as product_models
from django.utils.html import mark_safe


class rating(core_models.TimeStampedModel):

    rating_point = models.IntegerField(null=True) 

class Review(core_models.TimeStampedModel):
    
    product = models.ForeignKey("Products.product",  related_name = "Review", on_delete = models.CASCADE, null=True)
    user = models.ForeignKey("Users.user",  related_name = "Review", on_delete = models.CASCADE, null=True)
    rating = models.ForeignKey("rating", related_name = "Review", on_delete = models.CASCADE, null=True)
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=10)


    def rating_view(self):
        amount = 0
        datas = self.rating.all()
        print(datas)