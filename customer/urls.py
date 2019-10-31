from django.urls import path
from customer.views import customer_detail

app_name = 'customer'

urlpatterns = [
    path('', customer_detail, name='detail'),
]
