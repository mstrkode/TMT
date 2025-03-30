from django.urls import path

from interview.order.views import (DeactivateOrderView, OrderListCreateView,
                                   OrderTagListCreateView)

urlpatterns = [
    path("tags/", OrderTagListCreateView.as_view(), name="order-detail"),
    path("", OrderListCreateView.as_view(), name="order-list"),
    path(
        "deactivate/<int:order_id>/",
        DeactivateOrderView.as_view(),
        name="deactivate-order",
    ),
]
