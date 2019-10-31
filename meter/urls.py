from django.urls import path
from meter.views import meter_detail, meter_graph, meter_table

app_name = 'meter'

urlpatterns = [
    path('<int:pk>/', meter_detail, name="view_detail"),
    path('<int:pk>/graph/', meter_graph, name="view_graph"),
    path('<int:pk>/table/', meter_table, name="view_table"),
]