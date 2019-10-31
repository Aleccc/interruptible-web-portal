from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Meter
import json


class MeterList(ListView):
    model = Meter


@login_required
def meter_detail(request, pk):
    selected_meter = get_object_or_404(Meter, pk=pk)
    meters = Meter.objects.all()
    response = {'selected_meter': selected_meter,
                'meters': meters}
    return render(request, 'meter/detail.html', response)


@login_required
def meter_graph(request, pk):
    selected_meter = get_object_or_404(Meter, pk=pk)
    meters = Meter.objects.all()
    dates = [str(x.start_date) for x in selected_meter.meter_read.all()]
    dathm = [x.usage_dekatherm for x in selected_meter.meter_read.all()]
    response = {'selected_meter': selected_meter,
                'meters': meters,
                'graph_dates': json.dumps(dates),
                'graph_dathm': json.dumps(dathm),
                }
    return render(request, 'meter/graph.html', response)


@login_required
def meter_table(request, pk):
    selected_meter = get_object_or_404(Meter, pk=pk)
    meters = Meter.objects.all()
    response = {'selected_meter': selected_meter,
                'meter_reads': selected_meter.meter_read.all(),
                'meters': meters}
    return render(request, 'meter/table.html', response)
