from django.contrib import admin
from .import models
from django.utils.html import mark_safe
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, SliderNumericFilter


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    
    pass

@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    
    pass

@admin.register(models.Size)
class SizeAdmin(admin.ModelAdmin):
    
    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


class Product_inventory(admin.TabularInline):

    model = models.Product_inventory

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("__str__", 'get_thumbnail')

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}">')

    get_thumbnail.short_description = "Thumbnail"


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        user = request.user
        queryset = super(ProductAdmin, self).get_queryset(self)
        if user.is_superuser:
            return queryset
        return queryset.filter(created_by=user)


    def save_model(self, request, instance, form, change):
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.updated_by = user
        instance.save()
        form.save_m2m()
        return instance

    inlines = (PhotoInline, Product_inventory ,)
    

    list_display = (

        "photo",
        "product_name",
        "category",
        "gender",
        "price",
        "sale_price",
        "total_inventory",
        "sold_out_list",
    )

    list_filter = (
        "gender",
        "category",
        ("price", RangeNumericFilter),
    ) 

    search_fields = (  
        "product_name",        
    )



