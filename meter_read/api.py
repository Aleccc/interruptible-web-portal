from tastypie.resources import ModelResource
from tastypie.contrib.contenttypes.fields import GenericForeignKeyField
from tastypie.authorization import DjangoAuthorization
from meter.models import Meter
from meter.api import MeterResource
from .models import MeterRead


class MeterReadResource(ModelResource):
    content_object = GenericForeignKeyField({
        Meter: MeterResource,
    }, 'content_object')

    class Meta:
        queryset = MeterRead.objects.all()
        allowed_methods = ['get', 'post', 'put']
        authorization = DjangoAuthorization()
