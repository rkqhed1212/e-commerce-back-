from django.db import models
from core import models as core_models
from Users import models as user_models


class FQA(core_models.TimeStampedModel):
    
    user = models.ForeignKey("Users.user",  related_name = "FQA", on_delete = models.CASCADE, null=True)
    title = models.CharField(max_length=10, null = True)
    content = models.CharField(max_length=10, null = True)
    order_number = models.IntegerField()
