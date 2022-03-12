from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Zone

@registry.register_document
class ZoneDocument(Document):
    class Index:
        name = 'zone'
        
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    
    class Django:
        model = Zone
        
        fields = [
            'zip_code',
        ]

    def get_queryset(self):
        return super(ZoneDocument, self).get_queryset().select_related(
            'zone'
        )