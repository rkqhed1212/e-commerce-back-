from django.db import models
from core import models as core_models
from Users import models as user_models
from django.utils.html import mark_safe

class AbstractItem(core_models.TimeStampedModel):

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(AbstractItem):
    
    class Meta:
        verbose_name = "category"
        ordering = ['created'] 


class Size(AbstractItem):

    class Meta:
        verbose_name = "size"
        ordering = ['created']


class Color(AbstractItem):
    class Meta:
        verbose_name = "color"
        ordering = ['created']


class Photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=80 , blank=True)
    product = models.ForeignKey("Product",  related_name = "Photo", on_delete = models.CASCADE)
    file = models.ImageField(upload_to = "product_photos")

    def __str__(self):
        return self.caption

class Product_inventory(core_models.TimeStampedModel):
    
    product = models.ForeignKey("Product",  related_name = "Product_inventory", on_delete = models.CASCADE, null=True)
    inventory = models.IntegerField(null=True) 
    color = models.ForeignKey("color",  related_name = "Product_inventory", on_delete = models.CASCADE)
    size = models.ForeignKey("size",  related_name = "Product_inventory", on_delete = models.CASCADE)



class Product(core_models.TimeStampedModel, core_models.UserpermissionModel):


    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_CHOICSES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female")
    )


    product_name = models.TextField()
    product_description = models.TextField()
    category = models.ForeignKey("category",  related_name = "Product", on_delete = models.CASCADE)
    gender = models.CharField(choices = GENDER_CHOICSES, max_length=10, null = True)
    price = models.IntegerField(help_text="original price",null=True, blank=False)
    sale_price = models.IntegerField(null=True, blank=False)
    

    def __str__(self):
        return self.product_name

    def total_inventory(self):
        amount = 0
        datas = self.Product_inventory.all()
        for data in datas:
            amount += data.inventory 
        return amount

    def sold_out_list(self):
        datas = self.Product_inventory.all()
    
        sold_out_cnt = 0
        str_inven = ""
        for idx, data in enumerate(datas):

            if data.inventory == 0 :
                str_inven += f"{data.size.name}, "
                str_inven += f"{data.color.name} / "
                sold_out_cnt += 1
            
                

        if sold_out_cnt > 3:
            return f"{sold_out_cnt} items sold out"
        elif sold_out_cnt == 0:
            return "All items available"
        else:
            len_str = len(str_inven)
            return f"{str_inven[:len_str-2]} || Out of stock"

    def photo(self):
        try:
            (datas,) = self.Photo.all()[:1]
            return mark_safe(f'<img width="50px" src="{datas.file.url}">')
        except Exception:
            return None
    
    def color_lists(self):
        inven_list = self.Product_inventory.all()
        color_list = []
        for item in inven_list:
            color_list.append(item.color.name)
        color_set = set(color_list)
        return color_set


    def size_lists(self):
        inven_list = self.Product_inventory.all()
        size_list = []
        for item in inven_list:
            size_list.append(item.size.name)
        size_set = set(size_list)
        return size_set



