from django.contrib import admin
from .models import Device

# Acción personalizada para activar dispositivos
@admin.action(description="Activar dispositivos seleccionados")
def make_active(modeladmin, request, queryset):
    queryset.update(status="ACTIVE")

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    # Columnas a mostrar
    list_display = ("name", "organization", "zone", "status")
    # Campos para buscar
    search_fields = ("name", "organization__name", "zone__name")
    # Filtros en la barra lateral
    list_filter = ("organization", "zone")
    # Optimización de relaciones ForeignKey
    list_select_related = ("organization", "zone")
    # Orden por defecto
    ordering = ("organization__name", "name")
    # Acciones personalizadas
    actions = [make_active]
