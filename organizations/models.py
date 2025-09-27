from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=150, unique=True)
    def __str__(self): return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="members")
    def __str__(self): return f"{self.user.username} — {self.organization.name}"

# === NUEVO ===
class Zone(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="zones")
    name = models.CharField(max_length=120)

    class Meta:
        unique_together = ("organization", "name")

    def __str__(self):
        return f"{self.name} @ {self.organization.name}"
