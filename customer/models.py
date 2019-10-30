from django.db import models
from django.contrib.auth.models import User
from meter.models import Meter


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    meters = models.ManyToManyField(Meter)

    def __str__(self):
        return '%s (%s)' % (self.user.get_full_name(), self.user)
