from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class MeterRead(models.Model):
    read_month = models.CharField(max_length=64, blank=True)
    usage_ccf = models.FloatField()
    usage_dekatherm = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    design_day_mcf = models.FloatField()
    design_day_dekatherm = models.FloatField()
    read_source = models.CharField(max_length=64, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return '%s' % self.read_month

    def clean(self):
        # Don't allow start_date to occur on or after end_date
        if self.start_date > self.end_date:
            raise ValidationError(_('Start Date cannot occur on or after End Date.'))
