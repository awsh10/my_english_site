from django.db import models
from django.utils import timezone


class EnglishWord(models.Model):
    english = models.CharField(primary_key=True,
                               max_length=50)
    transcription = models.CharField(max_length=30)
    russian = models.CharField(max_length=250)
    date = models.DateTimeField(default=timezone.now)
    access_count = models.IntegerField(default=0)

    '''    def save(self, *args, **kwargs):
        super().save()
        if kwargs.get('save_statistics', True):
            statistic_obj = Statistics(english=self)
            statistic_obj.date = self.date
            statistic_obj.save()
    '''
    def __str__(self):
        return '{} --- {}'.format(self.english, self.russian)


class Statistics(models.Model):
    english_word = models.ForeignKey('EnglishWord', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    access_count = models.IntegerField(default=0)

    #def __init__(self, english, *args, **kwargs):
     #   print('kwargs - {}'.format(kwargs))

    def __str__(self):
        return '{} {} {} '.format(self.english_word.english, self.date, self.access_count)

    def save(self, *args, **kwargs):
        super().save()
        en_words = Statistics.objects.filter(english_word=self.english_word)
        self.access_count = len(en_words)
        self.english_word.access_count = self.access_count
        self.english_word.save()
        super().save()

    def search(self, english_word):
        en_word = EnglishWord.objects.get(english=english_word)
        if en_word:
            self.access_count = len(en_word.english_words.all())
        else:
            print('No ehglish word')
