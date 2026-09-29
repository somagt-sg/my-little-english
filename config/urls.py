from django.contrib import admin
from django.urls import path

from juego import views


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.inicio, name="inicio"),

    path(
        "habitacion/",
        views.habitacion,
        name="habitacion"
    ),
]