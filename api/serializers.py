from rest_framework import serializers
from zones.models import Zone

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ["zip_code", "level_of_litter", "times_reported",]

