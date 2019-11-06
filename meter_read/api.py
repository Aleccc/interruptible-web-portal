from tastypie.resources import ModelResource
from tastypie.contrib.contenttypes.fields import GenericForeignKeyField
from meter.models import Meter
from meter.api import MeterResource
from .models import MeterRead


class MeterReadResource(ModelResource):
    content_object = GenericForeignKeyField({
        Meter: MeterResource,
    }, 'content_type')

    class Meta:
        queryset = MeterRead.objects.all()
