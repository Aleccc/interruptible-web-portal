from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from meter_read.models import MeterRead
from .models import Meter


class MeterReadInline(GenericTabularInline):
    model = MeterRead
    extra = 0
    classes = ['collapse']


@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    search_fields = ['meter', 'gas_south_account_number', 'ldc_account_number', 'premise_number']
    list_filter = ('location',)
    inlines = [
        MeterReadInline,
    ]