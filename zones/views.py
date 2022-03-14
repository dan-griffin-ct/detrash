from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages

from .models import Zone
import zipcodes

class ZoneCreateView(TemplateView):
    template_name = 'zones/create_zone.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        zip_code = request.POST['zip_code']
        validated_zip_code = zipcodes.matching(zip_code)

        if validated_zip_code:
            zone, created = Zone.objects.update_or_create(zip_code=zip_code, defaults={'level_of_litter': request.POST['level_of_litter'],
                                                                                       'city': validated_zip_code[0]['city'],
                                                                                       'reported_by': request.user.email})
        else:
            messages.add_message(request, messages.INFO, 'Shoot! Please try entering a valid zip code to create a new Zone.')

        return HttpResponseRedirect('/zones/list/')


class ZoneListView(TemplateView):
    
    template_name = 'zones/list_zone.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ZipCodeLookupView(View):
    
    def get(self, request, *args, **kwargs):
        print(f"get - {request.GET['zip_code']}")
        zip_code = request.GET['zip_code']

        data = zipcodes.matching(zip_code)

        return JsonResponse(data, safe=False, content_type='application/json')
