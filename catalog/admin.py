from django.contrib import admin
from .forms import ProductAlertRuleForm
from .models import Category, Product, AlertRule, ProductAlertRule

# Inline para ProductAlertRule (editar hijos desde Product)
class ProductAlertRuleInline(admin.TabularInline):
    model = ProductAlertRule
    form = ProductAlertRuleForm      # ← usa el form con la validación
    extra = 0
    fields = ("alert_rule", "threshold_min", "threshold_max")
    show_change_link = True

# Admin de Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
    list_per_page = 50

# Admin de Product con Inline
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "category")
    search_fields = ("name", "sku", "category__name")
    list_filter = ("category",)
    list_select_related = ("category",)
    ordering = ("name",)
    inlines = [ProductAlertRuleInline]

# Admin de AlertRule
@admin.register(AlertRule)
class AlertRuleAdmin(admin.ModelAdmin):
    list_display = ("name", "severity", "description")
    search_fields = ("name",)
    list_filter = ("severity",)
    ordering = ("name",)

# Admin de ProductAlertRule con formulario y validaciones
@admin.register(ProductAlertRule)
class ProductAlertRuleAdmin(admin.ModelAdmin):
    form = ProductAlertRuleForm      # ← también aquí
    list_display = ("product", "alert_rule", "threshold_min", "threshold_max")
    list_filter = ("alert_rule__severity",)
    search_fields = ("product__name", "product__sku", "alert_rule__name")
    list_select_related = ("product", "alert_rule")
    ordering = ("product__name",)
