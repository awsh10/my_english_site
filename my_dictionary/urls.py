from django.conf.urls import url

from .views import DictionaryView, FindEnglishWordView, ErrorView

urlpatterns = [
    url(r'^$', DictionaryView.as_view(), name='dictionary'),
    url(r'^(?P<english_word>[a-z]*)/$', FindEnglishWordView.as_view(), name='find'),
    url(r'^(?P<path>.*)/$', ErrorView.as_view()),
]

