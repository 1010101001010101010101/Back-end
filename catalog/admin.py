from django.contrib import admin
from .models import Category, Product, AlertRule, ProductAlertRule

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(AlertRule)
@admin.register(ProductAlertRule)
class ProductAlertRuleAdmin(admin.ModelAdmin):
    list_display = ("product","alert_rule","threshold_min","threshold_max")
    list_filter = ("product","alert_rule")
