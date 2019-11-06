from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
# from tastypie.fields import ToManyField
from tastypie.resources import ModelResource

from .models import Meter


class MeterResource(ModelResource):
    # meter_read = ToManyField('meter_read.api.MeterReadResource',
    #                          'meter_read', full=True, null=True, blank=True)

    class Meta:
        queryset = Meter.objects.all()
        allowed_methods = ['get', 'post', 'put']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
