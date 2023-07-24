from django.shortcuts import render
from django.views.generic import ListView, TemplateView, FormView

from account.models import Customer

class AdminDashboard(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'account/admin_dashboard.html'

    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(is_staff=False)

    def get_context_data(self, **kwargs):
       context = super(AdminDashboard, self).get_context_data(**kwargs)
       return context


class CustomerDashboard(TemplateView):
    template_name = 'account/customer_dashboard.html'
