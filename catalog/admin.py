from django.contrib import admin
from .models import Category, Product, AlertRule, ProductAlertRule

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
    list_per_page = 50

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "category")
    search_fields = ("name", "sku", "category__name")
    list_filter = ("category",)
    list_select_related = ("category",)
    ordering = ("name",)

@admin.register(AlertRule)
class AlertRuleAdmin(admin.ModelAdmin):
    list_display = ("name", "severity", "description")
    search_fields = ("name",)
    list_filter = ("severity",)           # <— filtro por severidad
    ordering = ("name",)

@admin.register(ProductAlertRule)
class ProductAlertRuleAdmin(admin.ModelAdmin):
    list_display = ("product", "alert_rule", "threshold_min", "threshold_max")
    search_fields = ("product__name", "product__sku", "alert_rule__name")
    list_filter = ("alert_rule__severity", "product__category")  # <— por severidad (FK)
    list_select_related = ("product", "alert_rule")
    ordering = ("product__name",)