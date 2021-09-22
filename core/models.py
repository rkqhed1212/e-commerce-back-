from django.db import models
from django.db.models.deletion import SET_NULL


class TimeStampedModel(models.Model):

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)


    class Meta:
        abstract = True


class UserpermissionModel(models.Model):

    created_by = models.ForeignKey("Users.user",related_name = "UserpermissionModel", on_delete=SET_NULL,null=True, blank= True)
    updated_by = models.ForeignKey("Users.user", related_name = "UserpermissionModel2", on_delete=SET_NULL, null=True,blank= True)


    class Meta:
        abstract = True
