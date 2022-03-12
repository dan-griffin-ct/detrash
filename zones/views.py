from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect

from .models import Zone

class ZoneCreateView(TemplateView):
    template_name = 'zones/create_zone.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        print(f'self {self} request {request.POST}')
        zone, created = Zone.objects.update_or_create(zip_code=request.POST['zip_code'], defaults={'level_of_litter': request.POST['level_of_litter']})
        print(f'{created}, zone {zone}')

        return HttpResponseRedirect('/zones/list/')


class ZoneListView(ListView):
    
    template_name = 'zones/list_zone.html'

    model = Zone
    paginate_by = 25  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
