from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Measurement, AlertEvent
from catalog.models import ProductAlertRule

@receiver(post_save, sender=Measurement)
def evaluate_alerts(sender, instance: Measurement, created, **kwargs):
    if not created:
        return
    for par in ProductAlertRule.objects.filter(product=instance.product):
        low = (par.threshold_min is not None and instance.value < par.threshold_min)
        high = (par.threshold_max is not None and instance.value > par.threshold_max)
        if low or high:
            detail = []
            if low:  detail.append(f"value {instance.value} < min {par.threshold_min}")
            if high: detail.append(f"value {instance.value} > max {par.threshold_max}")
            AlertEvent.objects.create(measurement=instance, rule=par.alert_rule, detail="; ".join(detail))
