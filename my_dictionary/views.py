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


def insert_word(english_word, transcription=None, russian_word=None):
    try:
        EnglishWord(english_word=english_word, transcription=transcription, russian_word=russian_word)
        msg = 'Word "{} have been inserted!'.format(english_word)
    except:
        msg = 'The word "{}" have been inserted to the dictioanary early!'.format(english_word)
    return msg

def english_word_strip(english_word):
    length = len(english_word)
    old_word = english_word
    words_list = english_word.split()

    english_word = ''
    for i in range(len(words_list)):
        english_word += words_list[i] + ' '
    #english_word = english_word.strip()
    #print('old word - "{}" length = {}, new word "{}" - len {}'.format(old_word, length, english_word, len(english_word)))
    return english_word.strip()


class InsertWordView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            english_word = request.POST['englishWord']
            msg = insert_word(english_word_strip(english_word))
            data = {'english_word': english_word_strip(english_word)}
            return HttpResponse(json.dumps(msg))
