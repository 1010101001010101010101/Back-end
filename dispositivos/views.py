from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Device

@login_required
def dashboard(request):
    return render(request, "dispositivos/dashboard.html")

@login_required
def devices_list(request):
    org = request.user.userprofile.organization  # relación User -> UserProfile -> Organization
    qs = Device.objects.filter(organization=org).order_by("name")
    return render(request, "dispositivos/list.html", {"devices": qs})
