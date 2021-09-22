from django.contrib import admin
from .import models



@admin.register(models.Points)
class PointAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "user",
        "amount",
        "content"
    )

