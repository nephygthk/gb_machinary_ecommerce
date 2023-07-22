from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from store.models import Product

class HomeView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'frontend/index.html'


class AboutView(TemplateView):
    template_name = 'frontend/about.html'