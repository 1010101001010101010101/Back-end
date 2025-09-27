from django.core.management.base import BaseCommand
from catalog.models import Category, Product, AlertRule, ProductAlertRule

class Command(BaseCommand):
    help = "Carga 2 categorías, 3 productos y reglas de alerta con umbrales"

    def handle(self, *args, **kwargs):
        # Categorías
        lighting, _ = Category.objects.get_or_create(name="Lighting")
        hvac, _ = Category.objects.get_or_create(name="HVAC")

        # Productos (3)
        p1, _ = Product.objects.get_or_create(name="LED Panel 40W", sku="LED-40W",  category=lighting)
        p2, _ = Product.objects.get_or_create(name="LED Bulb 12W",  sku="LED-12W",  category=lighting)
        p3, _ = Product.objects.get_or_create(name="Extractor 100W", sku="HVAC-100W", category=hvac)

        # Reglas de alerta (2)
        high, _ = AlertRule.objects.get_or_create(name="Consumo alto", defaults={"description":"kWh por encima del umbral"})
        low,  _ = AlertRule.objects.get_or_create(name="Consumo bajo",  defaults={"description":"kWh por debajo del umbral"})

        # Umbrales por producto (distintos)
        ProductAlertRule.objects.get_or_create(product=p1, alert_rule=high, defaults={"threshold_max": 100})
        ProductAlertRule.objects.get_or_create(product=p1, alert_rule=low,  defaults={"threshold_min": 5})

        ProductAlertRule.objects.get_or_create(product=p2, alert_rule=high, defaults={"threshold_max": 60})
        ProductAlertRule.objects.get_or_create(product=p2, alert_rule=low,  defaults={"threshold_min": 2})

        ProductAlertRule.objects.get_or_create(product=p3, alert_rule=high, defaults={"threshold_max": 200})
        ProductAlertRule.objects.get_or_create(product=p3, alert_rule=low,  defaults={"threshold_min": 10})

        self.stdout.write(self.style.SUCCESS("Seed catálogo OK: 2 categorías, 3 productos, 2 reglas y umbrales"))
