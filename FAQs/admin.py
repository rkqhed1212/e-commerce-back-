from django.contrib import admin
from . import models



@admin.register(models.FQA)
class FQAAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "title",
        "content",
        "order_number"
    )
