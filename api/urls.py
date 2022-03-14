from django.urls import path, include
from .views import ZoneListApiView, ZoneDetailApiView

urlpatterns = [
    path('zones', ZoneListApiView.as_view(), name='api-zone-list'),
    path('zones/<int:zone_id>/', ZoneDetailApiView.as_view(), name='api-zone-detail'),
    ]
