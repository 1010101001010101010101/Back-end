from django.contrib import admin
from .models import Measurement, AlertEvent

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "device", "product", "value")
    search_fields = ("device__name", "product__name", "product__sku")
    list_filter = ("device__organization", "product", "device")
    list_select_related = ("device", "product")
    date_hierarchy = "timestamp"
    ordering = ("-timestamp",)

@admin.register(AlertEvent)
class AlertEventAdmin(admin.ModelAdmin):
    list_display = ("triggered_at", "rule", "measurement", "detail")
    search_fields = ("rule__name", "measurement__device__name", "detail")
    list_filter = ("rule",)
    list_select_related = ("measurement", "rule")
    date_hierarchy = "triggered_at"
    ordering = ("-triggered_at",)
