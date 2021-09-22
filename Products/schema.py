import graphene
from graphene_django import DjangoObjectType,DjangoListField
from Products.models import Product, Product_inventory, Color, Size, Category, Photo


class CategorySerializer(DjangoObjectType):

    class Meta:
        model = Category
        fields = ('name',)


class Color(DjangoObjectType):

    class Meta:
        model = Color
        fields = ('name',)

class Size(DjangoObjectType):

    class Meta:
        model = Size
        fields = ('name',)

class Photo(DjangoObjectType):

    class Meta: 
        model = Photo
        fields= ('caption','file')

    def resolve_file(self,info):
        if self.file:
            self.file = info.context.build_absolute_uri(self.file.url)
        return self.file   
    
class Product(DjangoObjectType):

    class Meta: 
        model = Product
        fields = ('product_name', 'product_description', 'category' ,'gender','price','sale_price','Photo')

class InventoryType(DjangoObjectType):

    product = graphene.Field(Product)
    color = graphene.Field(Color)
    size = graphene.Field(Size)
    Photo = graphene.Field(Photo)

    class Meta:
        model = Product_inventory
        fields = (
            'id',
            'Photo',
            'color',
            'size',
            'inventory',
            'product',
        )


class ProductListresponse(graphene.ObjectType):

    arr = graphene.List(InventoryType)
    total = graphene.Int()

class Query(graphene.ObjectType):


    Product_inventory = graphene.Field(ProductListresponse, page=graphene.Int())
    InventoryList = graphene.List(InventoryType)

    def resolve_Product_inventory(self, info, page=1):
        page_size = 10 
        skipping = page_size * (page-1)
        taking =  page_size * page
        proudcts = Product_inventory.objects.all()[skipping:taking]
        total = Product_inventory.objects.count()
        return ProductListresponse(arr = proudcts, total = total)

    
    def resolve_InventoryList(root,info):
        return Product_inventory.objects.all()



schema = graphene.Schema(query=Query)