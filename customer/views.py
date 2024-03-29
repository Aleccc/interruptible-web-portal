from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from customer.models import Customer


@login_required
def customer_detail(request):
    customer = request.user.customer
    customer = get_object_or_404(Customer, pk=customer.pk)
    response = {'customer': customer,
                }
    return render(request, 'customer/detail.html', response)
