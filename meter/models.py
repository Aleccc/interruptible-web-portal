from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

from .utils import LOCATION_CHOICES, ATL
from meter_read.models import MeterRead


class Meter(models.Model):
    meter = models.CharField(max_length=64)
    gas_south_account_number = models.CharField(max_length=64)
    ldc_account_number = models.CharField('LDC account number', max_length=64, blank=True)
    premise_number = models.CharField(max_length=64, blank=True)
    location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        default=ATL,
    )
    county = models.CharField(max_length=64, blank=True)
    record_type = models.CharField(max_length=64, blank=True)
    meter_read = GenericRelation(MeterRead)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
