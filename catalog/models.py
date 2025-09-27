from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    def __str__(self): return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    def __str__(self): return f"{self.name} ({self.sku})"

class AlertRule(models.Model):
    SEVERITY_CHOICES = [
        ("info", "Informativa"),
        ("warn", "Advertencia"),
        ("crit", "Crítica"),
    ]
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    severity = models.CharField(max_length=5, choices=SEVERITY_CHOICES, default="warn")

    def __str__(self):
        return self.name


class ProductAlertRule(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="alert_rules")
    alert_rule = models.ForeignKey(AlertRule, on_delete=models.CASCADE, related_name="product_links")
    threshold_min = models.FloatField(null=True, blank=True)
    threshold_max = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ("product", "alert_rule")

    def __str__(self):
        return f"{self.product} -> {self.alert_rule}"
