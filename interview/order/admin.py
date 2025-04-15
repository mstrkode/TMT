from django.contrib import admin
from .models import Order, OrderTag


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "inventory", "start_date", "embargo_date", "is_active"]
    list_filter = ["is_active", "start_date", "embargo_date"]
    search_fields = ["inventory__name"]


class OrderTagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["name"]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderTag, OrderTagAdmin)
