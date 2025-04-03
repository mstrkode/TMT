from django.urls import path

from interview.order.views import (
    DeactivateOrderView,
    OrderListCreateView,
    OrdersBetweenDatesView,
    OrderTagListCreateView,
)

urlpatterns = [
    path("tags/", OrderTagListCreateView.as_view(), name="order-detail"),
    path("", OrderListCreateView.as_view(), name="order-list"),
    path(
        "deactivate/<int:order_id>/",
        DeactivateOrderView.as_view(),
        name="deactivate-order",
    ),
    path(
        "between-dates/", OrdersBetweenDatesView.as_view(), name="orders-between-dates"
    ),
]
