from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=120)
    organization = models.ForeignKey("organizations.Organization", on_delete=models.PROTECT)
    zone = models.ForeignKey("organizations.Zone", on_delete=models.PROTECT, null=True, blank=True)
    
    STATUS_CHOICES = [
        ("ACTIVE", "Activo"),
        ("INACTIVE", "Inactivo"),
    ]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="INACTIVE")

    def __str__(self):
        return self.name
