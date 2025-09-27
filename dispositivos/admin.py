from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "zone")
    search_fields = ("name", "organization__name", "zone__name")
    list_filter = ("organization", "zone")
    list_select_related = ("organization", "zone")
    ordering = ("organization__name", "name")
