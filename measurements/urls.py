from django.urls import path
from . import views
urlpatterns = [ path("lecturas/", views.measurement_list, name="measurement_list"), ]
