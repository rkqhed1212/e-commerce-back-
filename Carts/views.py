from rest_framework.generics import ListAPIView, RetrieveAPIView
from Carts.models import Cart 
from .serializers import CartSerializer


class CartsListView(ListAPIView):

    queryset = Cart.objects.all()

    serializer_class = CartSerializer
    
    
class CartsDetailView(RetrieveAPIView):

    queryset = Cart.objects.all()

    serializer_class = CartSerializer



