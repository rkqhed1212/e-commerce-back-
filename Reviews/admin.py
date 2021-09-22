from django.contrib import admin
from . import models




@admin.register(models.rating)
class ratingAdmin(admin.ModelAdmin):
    model = models.rating


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    

    list_display = (
        "product",
        "user",
        "title",
        "content"
    )

