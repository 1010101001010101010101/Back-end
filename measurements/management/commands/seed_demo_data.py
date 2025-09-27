from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from organizations.models import Organization, UserProfile, Zone
from dispositivos.models import Device
from catalog.models import Product
from measurements.models import Measurement

User = get_user_model()

class Command(BaseCommand):
    help = "Crea 1 org, 2 zonas, 3 dispositivos y lecturas demo (disparan alertas)"

    def handle(self, *args, **kwargs):
        u = User.objects.get(username="keyla")
        org, _ = Organization.objects.get_or_create(name="Mi Empresa")
        UserProfile.objects.get_or_create(user=u, defaults={"organization": org})

        z1, _ = Zone.objects.get_or_create(organization=org, name="Zona 1")
        z2, _ = Zone.objects.get_or_create(organization=org, name="Zona 2")

        d1, _ = Device.objects.get_or_create(name="Sensor A",  organization=org, defaults={"zone": z1})
        d2, _ = Device.objects.get_or_create(name="Cámara B",  organization=org, defaults={"zone": z2})
        d3, _ = Device.objects.get_or_create(name="Medidor C", organization=org, defaults={"zone": z1})

        p1 = Product.objects.get(sku="LED-40W")
        p2 = Product.objects.get(sku="LED-12W")
        p3 = Product.objects.get(sku="HVAC-100W")

        # Lecturas (usan get_or_create para no duplicar si corres el seed de nuevo)
        for v in [3, 8, 120]:    # p1: 3 -> bajo, 120 -> alto
            Measurement.objects.get_or_create(device=d1, product=p1, value=v)
        for v in [10, 55, 70]:   # p2: 70 -> alto
            Measurement.objects.get_or_create(device=d2, product=p2, value=v)
        for v in [5, 15, 250]:   # p3: 5 -> bajo, 250 -> alto
            Measurement.objects.get_or_create(device=d3, product=p3, value=v)

        self.stdout.write(self.style.SUCCESS("Demo OK: 1 org, 2 zonas, 3 devices, lecturas con alertas"))
