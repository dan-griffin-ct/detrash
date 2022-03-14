from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from zones.models import Zone
from .serializers import ZoneSerializer
import zipcodes

class ZoneListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        # List all the todo items for given requested user
        zones = Zone.objects.all().order_by('times_reported')
        serializer = ZoneSerializer(zones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        # Create the Zone with given zone data

        validated_zip_code = zipcodes.matching(request.data.get('zip_code'))
        if validated_zip_code:
            data = {
                'zip_code': request.data.get('zip_code'), 
                'city': request.data.get('city'), 
                'level_of_liter': request.data.get('level_of_litter'),
                'user': request.user.email
            }
            serializer = ZoneSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ZoneDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, zone_id):
        # Helper method to get the object with given zone_id
        try:
            return Zone.objects.get(id=zone_id)
        except Zone.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, zone_id, *args, **kwargs):
        '''
        Retrieves the Zone with given zone_id
        '''
        zone_instance = self.get_object(zone_id)
        if not zone_instance:
            return Response(
                {"res": "Object with zone id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ZoneSerializer(zone_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, zone_id, *args, **kwargs):
        # Updates the zone item with given zone_id if exists
        print(request.data.get('level_of_litter'))
        zone_instance = self.get_object(zone_id)
        if not zone_instance:
            return Response(
                {"res": "Object with zone id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'level_of_litter': request.data.get('level_of_litter'), 
        }
        serializer = ZoneSerializer(instance = zone_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
