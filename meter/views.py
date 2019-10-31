from django.shortcuts import get_object_or_404, render
from .models import Meter


def meter_detail(request, pk):
    selected_meter = get_object_or_404(Meter, pk=pk)
    meters = Meter.objects.all()
    response = {'selected_meter': selected_meter,
                'meters': meters}
    return render(request, 'meter/detail.html', response)


def meter_graph(request, pk):
    selected_meter = get_object_or_404(Meter, pk=pk)
    meters = Meter.objects.all()
    response = {'selected_meter': selected_meter,
                'meters': meters,
                'labels': [str(x.start_date) for x in selected_meter.meter_read.all()],
                'dathm': [x.usage_dekatherm for x in selected_meter.meter_read.all()],
                }
    return render(request, 'meter/graph.html', response)
