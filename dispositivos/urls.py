from django.urls import path
from . import views

urlpatterns = [
    path("lista/", views.devices_list, name="devices_list"),
]
