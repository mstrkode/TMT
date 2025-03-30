from django.urls import path

from interview.inventory.views import (
    InventoryLanguageListCreateView,
    InventoryLanguageRetrieveUpdateDestroyView,
    InventoryListView,
    InventoryRetrieveUpdateDestroyView,
    InventoryTagListCreateView,
    InventoryTagRetrieveUpdateDestroyView,
    InventoryTypeListCreateView,
    InventoryTypeRetrieveUpdateDestroyView,
)

urlpatterns = [
    path(
        "<int:id>/",
        InventoryRetrieveUpdateDestroyView.as_view(),
        name="inventory-detail",
    ),
    path(
        "languages/<int:id>/",
        InventoryLanguageRetrieveUpdateDestroyView.as_view(),
        name="inventory-languages-detail",
    ),
    path(
        "tags/<int:id>/",
        InventoryTagRetrieveUpdateDestroyView.as_view(),
        name="inventory-tags-detail",
    ),
    path(
        "types/<int:id>/",
        InventoryTypeRetrieveUpdateDestroyView.as_view(),
        name="inventory-types-detail",
    ),
    path(
        "languages/",
        InventoryLanguageListCreateView.as_view(),
        name="inventory-languages-list",
    ),
    path("tags/", InventoryTagListCreateView.as_view(), name="inventory-tags-list"),
    path("types/", InventoryTypeListCreateView.as_view(), name="inventory-types-list"),
    path("inventory/", InventoryListView.as_view(), name="inventory-list"),
]
