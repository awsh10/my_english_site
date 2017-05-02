from datetime import datetime
from django.test import TestCase
from django.utils import timezone

from my_dictionary.models import EnglishWord, Statistics


class EnglishWordTestCase(TestCase):

    def setUp(self):
        self.english_words_list = ['invoke', 'troughout']
        self.russian_words_list = [['вызывать', 'активизировать', 'запускать'],
                              ['через', 'на всем протяжении', 'везде, все время']]
        self.month_day_hour_minute_list = [[[1, 12, 21, 22],[2, 21, 11, 22]],
                                           [[1, 1, 14, 6],[4, 15,  18, 10],
                                            [9, 4, 17, 55], [12, 11, 21, 21]]]
        year, accesses_count = 2016, []

        def insert_word(english_word, russian_word, date_time=None):
            english_word_obj = EnglishWord(english=english_word, russian=russian_word)
            if date_time:
                english_word_obj.date = date_time
            english_word_obj.save()

            #statistic_obj = english_word_obj.statistics_set.get(english=english_word_obj.english)
            #statistic_obj.date = english_word_obj.date
            #statistic_obj.save()
            return english_word_obj

        english_word_obj = None
        for num, english_word in enumerate(self.english_words_list):
            m_d_h_m_list = self.month_day_hour_minute_list[num:num + 1][0]
            if m_d_h_m_list:
                for i, m_d_h_m in enumerate(m_d_h_m_list):
                    month, day, hour, minute = m_d_h_m[0], m_d_h_m[1], m_d_h_m[2], m_d_h_m[3]
                    date_time = timezone.make_aware(datetime(year, month, day, hour, minute))
                    if i == 0:
                        english_word_obj = insert_word(english_word, self.russian_words_list[num], date_time)
                    else:
                        statistic_obj = Statistics(english_word=english_word_obj, date=date_time)
                        statistic_obj.save()
            else:
                insert_word(english_word, self.russian_words_list[num])

    def test_insert(self):
        english_words = [english_word_obj.english for english_word_obj in EnglishWord.objects.all()]
        self.assertEqual(english_words, self.english_words_list)

        for num, en_word in enumerate(EnglishWord.objects.all()):
            print(en_word, num)
            print(en_word.statistics_set.all())

        print(len(Statistics.objects.all()))

    ''''
    def test_insert_enlish_russian(self):

        for en_word in EnglishWord.objects.all():
            print(en_word, en_word.access_count)
            for st in en_word.statistics_set.all():
                print(st)

        for i in ():
            en_word = EnglishWord.objects.get(pk=i)
            self.assertEqual(en_word.english, self.english[i-1])
            self.assertEqual(en_word.russian, self.russian[i - 1])
    '''

'''
    def test_unique_record(self):
        try:
            EnglishWord.objects.create(english=self.english[1], russian=self.russian[1])
        except:
            print('\n Unique is True')

    def test_search_word(self):
        Statistics.search(self.english[0])
        if Statistics.count==2:
            print('Word is founded. Count = 2')

'''
