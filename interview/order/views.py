from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

class TagOrdersListView(APIView):
    def get(self, request, tag_id):
        try:
            tag = OrderTag.objects.get(id=tag_id)
            orders = tag.orders.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except OrderTag.DoesNotExist:
            return Response(
                {"error": "Tag not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
