from django.urls import path, include
from .views import ZoneListApiView

urlpatterns = [
    path('zones', ZoneListApiView.as_view(), name='api-zone-list'),
]
