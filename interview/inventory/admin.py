from django.contrib import admin
from .models import Inventory, InventoryLanguage, InventoryTag, InventoryType


class InventoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "type", "language"]
    list_filter = ["type", "language"]
    search_fields = ["name"]


class InventoryTagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["name"]


class InventoryLanguageAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


class InventoryTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(InventoryTag, InventoryTagAdmin)
admin.site.register(InventoryLanguage, InventoryLanguageAdmin)
admin.site.register(InventoryType, InventoryTypeAdmin)
