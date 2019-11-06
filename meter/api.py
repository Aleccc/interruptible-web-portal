from tastypie.resources import ModelResource
from .models import Meter


class MeterResource(ModelResource):
    class Meta:
        queryset = Meter.objects.all()
        allowed_methods = ['get']
