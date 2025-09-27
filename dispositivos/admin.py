from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("id","name","organization","zone")
    list_filter = ("organization","zone")
    search_fields = ("name",)
