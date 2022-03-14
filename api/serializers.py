from rest_framework import serializers
from zones.models import Zone

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ["zip_code", "city", "level_of_litter", "times_reported", "reported_by",]

