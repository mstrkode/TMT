from django.urls import path
from interview.order.views import (
    OrderListCreateView,
    OrderTagListCreateView,
    TagOrdersListView,
)


urlpatterns = [
    path("tags/", OrderTagListCreateView.as_view(), name="order-tags"),
    path("", OrderListCreateView.as_view(), name="order-list"),
    path(
        "tags/<int:tag_id>/orders/", TagOrdersListView.as_view(), name="tag-orders-list"
    ),
]
