from django.conf.urls import url

from .views import ExperimentView

urlpatterns = [
    url(r'^$',ExperimentView.as_view(), name='probability'),
]
