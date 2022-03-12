from django.urls import path
from zones.views import ZoneCreateView, ZoneListView

urlpatterns = [
    # ...
    path('create/', ZoneCreateView.as_view(), name='create-zone'),
    path('list/', ZoneListView.as_view(), name='list-zone'),
]