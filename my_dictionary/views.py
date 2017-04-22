import json

from django.http import HttpResponse
from django.views.generic.base import TemplateView, View

from my_dictionary.models import EnglishWord, Statistics


class DictionaryView(TemplateView):

    template_name = 'my_dictionary/dictionary.html'

    def get_context_data(self, **kwargs):
        context = super(DictionaryView, self).get_context_data(**kwargs)
        context['greeting'] = 'Hi, Anatolii'
        return context


class FindEnglishWordView(View):
    def get(self, request, **kwargs):
        try:
            en_word = EnglishWord.objects.get(pk=request.GET['englishWord'])
            data = {'english_word': en_word.english,
                    'transcription': en_word.transcription,
                    'russian_word': en_word.russian,
                    'access_count': en_word.access_count}
        except:
            data = False
        return HttpResponse(json.dumps(data))


class ErrorView(View):
    def get(self, request, **kwargs):
        if request.is_ajax:
            data = kwargs['path']
            return HttpResponse(json.dumps(data))


class InsertWordView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            data = {'1': 'I am glad'}
            return HttpResponse(json.dumps(data))