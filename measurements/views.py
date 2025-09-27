from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Measurement

@login_required
def measurement_list(request):
    org = request.user.userprofile.organization
    qs = Measurement.objects.filter(device__organization=org).select_related("device","product").order_by("-timestamp")[:200]
    return render(request, "measurements/list.html", {"measurements": qs})
