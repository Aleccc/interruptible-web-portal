from django.contrib import admin
from .models import MeterRead


@admin.register(MeterRead)
class MeterReadAdmin(admin.ModelAdmin):
    list_filter = ('start_date',)
