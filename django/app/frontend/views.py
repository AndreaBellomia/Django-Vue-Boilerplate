from django.views.generic import TemplateView
from django.shortcuts import render

class VueView(TemplateView):
    template_name = "frontend/index.html"