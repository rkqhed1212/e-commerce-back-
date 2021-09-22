from rest_framework.generics import ListAPIView, RetrieveAPIView
from Orders.models import Group_order
from .serializers import GroupSerializer


class OrderListView(ListAPIView):

    serializer_class = GroupSerializer
    
    def get_queryset(self):
        
        return Group_order.objects.filter(user=self.request.user)
    

    
class OrderDetailView(RetrieveAPIView):

    serializer_class = GroupSerializer

    def get_queryset(self):
        
        return Group_order.objects.filter(user=self.request.user)


