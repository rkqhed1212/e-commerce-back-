from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile", {"fields": ("nick_name","sns_type","gender", "birthday", "number","superhost")}
        ),
    )


    list_filter = UserAdmin.list_filter + ("superhost" ,)


    list_display = (
        "username",
        "first_name",
        "last_name",
        "nick_name",
        "sns_type",
        "number",
        "gender",
        "point",
        "email",
        "is_active",
        "superhost",
        "is_staff",
        "is_superuser",
    ) 
