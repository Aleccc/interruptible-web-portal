from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.contrib.contenttypes.fields import GenericForeignKeyField
from tastypie.resources import ModelResource

from meter.api import MeterResource
from meter.models import Meter
from .models import MeterRead


class AnonymousGetAuthentication(BasicAuthentication):
    """ No auth on get requests, BasicAuthentication for all else """

    def is_authenticated(self, request, **kwargs):
        """ If POST, don't check auth, otherwise fall back to parent """

        if request.method == "GET":
            return True
        else:
            return super(AnonymousPostAuthentication, self).is_authenticated(request, **kwargs)


class MeterReadResource(ModelResource):
    content_object = GenericForeignKeyField({
        Meter: MeterResource,
    }, 'content_object')

    class Meta:
        queryset = MeterRead.objects.all()
        allowed_methods = ['get', 'post']
        authentication = AnonymousGetAuthentication()
        authorization = DjangoAuthorization()
