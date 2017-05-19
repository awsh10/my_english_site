from django.db import models
from django.utils import timezone


class Experiment(models.Model):
    #class Meta():
    date = models.DateTimeField(default=timezone.now, unique=True)
    count = models.IntegerField(default=0)


class ExperimentData(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    date_ms = models.IntegerField(default=0)
    relative_date_ms = models.IntegerField(default=0)
