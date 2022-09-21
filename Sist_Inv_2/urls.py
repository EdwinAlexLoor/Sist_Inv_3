"""Sist_Inv URL Configuration

URL PRINCIPAL.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('control_inventario/', include("control_inventario.urls")),
    path('', include("autotenticacion.urls")),
]