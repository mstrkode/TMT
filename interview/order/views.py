from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class DeactivateOrderView(APIView):
    def post(self, request, order_id, *args, **kwargs):
        try:
            order = Order.objects.get(id=order_id)
            order.is_active = False
            order.save()
            return Response(
                {"message": "Order deactivated successfully."},
                status=status.HTTP_200_OK,
            )
        except Order.DoesNotExist:
            return Response(
                {"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND
            )


class OrdersBetweenDatesView(APIView):
    def get(self, request, *args, **kwargs):
        start_date = request.query_params.get("start_date")
        embargo_date = request.query_params.get("embargo_date")

        if not start_date or not embargo_date:
            return Response(
                {"error": "Both start_date and embargo_date are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        orders = Order.objects.filter(
            start_date__gte=start_date, embargo_date__lte=embargo_date
        )
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
