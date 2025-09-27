from django.contrib import admin
from .models import Measurement, AlertEvent
admin.site.register(Measurement)
admin.site.register(AlertEvent)
