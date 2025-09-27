from django.contrib import admin
from django.urls import path, include
from dispositivos.views import dashboard  # usamos la vista que ya tienes

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", dashboard, name="dashboard"),
    path("", include("accounts.urls")),
    path("dispositivos/", include("dispositivos.urls")),
    # Cuando tengas lista la app/urls de measurements, descomenta:
    path("mediciones/", include("measurements.urls")),
]
