from django.db import models
from organizations.models import Organization  # NO importes Zone aquí

class Device(models.Model):
    name = models.CharField(max_length=120)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="devices")
    # referencia diferida: "organizations.Zone"
    zone = models.ForeignKey("organizations.Zone", on_delete=models.PROTECT, related_name="devices", null=True, blank=True)

    def __str__(self):
        return self.name
