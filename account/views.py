from django.shortcuts import render
from django.views.generic import ListView, TemplateView, FormView
from django.http import HttpResponse

from account.models import Customer
from order.models import Order
from store.models import Product

class AdminDashboard(ListView):
   
   model = Customer
   context_object_name = 'customers'
   template_name = 'account/admin_dashboard.html'

   def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return HttpResponse("Error handler content", status=400)
        return super().dispatch(request, *args, **kwargs)

   def get_queryset(self, **kwargs):
      qs = super().get_queryset(**kwargs)
      return qs.filter(is_staff=False)

   def get_context_data(self, **kwargs):
      context = super(AdminDashboard, self).get_context_data(**kwargs)
      context['orders'] = Order.objects.all()
      context['products'] = Product.objects.all()[:9]
      return context


class CustomerDashboard(TemplateView):
    template_name = 'account/customer_dashboard.html'
