import json
import csv
from django.http import StreamingHttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Meter


class MeterList(LoginRequiredMixin, ListView):
    model = Meter

    def get_queryset(self):
        return self.request.user.customer.meters.all()


@login_required
def meter_detail(request, pk):
    selected_meter = get_object_or_404(Meter, pk=pk)
    meters = request.user.customer.meters.all()
    if selected_meter in meters:
        response = {'selected_meter': selected_meter,
                    }
    else:
        response = {'selected_meter': None,
                    }
    return render(request, 'meter/detail.html', response)


def _group_usage(queryset):
    import itertools
    dates = []
    dathm = []
    for key, group in itertools.groupby(queryset, lambda item: item['read_month']):
        dates.append(key)
        dathm.append(sum([item['city_gate_dekatherm'] for item in group]))
    return dates, dathm


@login_required
def meter_graph(request, pk):
    selected_meter = get_object_or_404(Meter, pk=pk)
    meters = request.user.customer.meters.all()
    if selected_meter in meters:
        dates = [str(x.start_date) for x in selected_meter.meter_read.all()]
        dathm = [x.city_gate_dekatherm for x in selected_meter.meter_read.all()]
        monthly_dates, monthly_dathm = _group_usage(selected_meter.meter_read.all().values())

        response = {'selected_meter': selected_meter,
                    'graph_dates': json.dumps(dates),
                    'graph_dathm': json.dumps(dathm),
                    'monthly_dates': json.dumps(monthly_dates),
                    'monthly_dathm': json.dumps(monthly_dathm),
                    }
    else:
        response = {'selected_meter': None,
                    'graph_dates': None,
                    'graph_dathm': None,
                    'monthly_dates': None,
                    'monthly_dathm': None,
                    }
    return render(request, 'meter/graph.html', response)


@login_required
def meter_table(request, pk):
    selected_meter = get_object_or_404(Meter, pk=pk)
    meters = request.user.customer.meters.all()
    if selected_meter in meters:
        response = {'selected_meter': selected_meter,
                    'meter_reads': selected_meter.meter_read.all().order_by('-start_date'),
                    }
    else:
        response = {'selected_meter': None,
                    'meter_reads': None,
                    }
    return render(request, 'meter/table.html', response)


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


@login_required
def export_csv(request, pk):
    selected_meter = get_object_or_404(Meter, pk=pk)
    meters = request.user.customer.meters.all()
    if selected_meter in meters:
        fieldnames = {'start_date': 'start_date', 'city_gate_dekatherm': 'city_gate_dekatherm'}
        meter_reads = list(selected_meter.meter_read.all().values(*fieldnames.keys()))
        meter_reads.insert(0, fieldnames)
        pseudo_buffer = Echo()
        writer = csv.DictWriter(pseudo_buffer, fieldnames=fieldnames.keys())
        response = StreamingHttpResponse((writer.writerow(row) for row in meter_reads),
                                         content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="meter_reads.csv"'
    else:
        response = None
    return response
