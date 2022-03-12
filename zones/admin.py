from django.contrib import admin
from .models import Zone

class ZoneAdmin(admin.ModelAdmin):
    list_display = ['zip_code', 'level_of_litter', 'times_reported']


admin.site.register(Zone, ZoneAdmin)
