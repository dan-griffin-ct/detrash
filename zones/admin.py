from django.contrib import admin
from .models import Zone

class ZoneAdmin(admin.ModelAdmin):
    list_display = ['zip_code', 'city', 'level_of_litter', 'times_reported', 'reported_by']


admin.site.register(Zone, ZoneAdmin)
