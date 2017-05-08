from django.conf.urls import url

from .views import DictionaryView, FindEnglishWordView, InsertWordView

urlpatterns = [
    url(r'^$', DictionaryView.as_view(), name='dictionary'),
    #url(r'^(?P<english_word>[a-z]*)/$', FindEnglishWordView.as_view(), name='find'),
    url(r'^find/$', FindEnglishWordView.as_view(), name='find', ),
    url(r'^insert/$', InsertWordView.as_view(), name='insert'),
]


