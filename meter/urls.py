from django.urls import path
from meter.views import MeterList, meter_detail, meter_graph, meter_table, export_csv

app_name = 'meter'

urlpatterns = [
    path('', MeterList.as_view(), name='list'),
    path('<int:pk>/', meter_detail, name="view_detail"),
    path('<int:pk>/graph/', meter_graph, name="view_graph"),
    path('<int:pk>/table/', meter_table, name="view_table"),
    path('<int:pk>/export/', export_csv, name="export"),
]