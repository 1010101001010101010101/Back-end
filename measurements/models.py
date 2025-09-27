from django.db import models
from django.utils import timezone
from dispositivos.models import Device
from catalog.models import Product, AlertRule, ProductAlertRule

class Measurement(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="measurements")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="measurements")
    timestamp = models.DateTimeField(default=timezone.now)
    value = models.FloatField()
    def __str__(self):
        return f"{self.device} {self.value} @ {self.timestamp:%Y-%m-%d %H:%M}"

class AlertEvent(models.Model):
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name="alerts")
    rule = models.ForeignKey(AlertRule, on_delete=models.CASCADE, related_name="events")
    triggered_at = models.DateTimeField(default=timezone.now)
    detail = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return f"ALERT {self.rule.name} on {self.measurement_id}"
