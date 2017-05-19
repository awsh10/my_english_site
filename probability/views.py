import json

from django.http import HttpResponse
from django.views.generic.base import TemplateView, View

from probability.models import Experiment

class ExperimentView(TemplateView):
    template_name ='probability/probability.html'