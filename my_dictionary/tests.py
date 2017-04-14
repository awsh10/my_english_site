from datetime import datetime
from django.test import TestCase
from django.utils import timezone

from my_dictionary.models import EnglishWord, Statistics


class EnglishWordTestCase(TestCase):

    def setUp(self):
        self.english_words, self.russian_words = ['invoke',
                                                  'troughout'],\
                                                 ['вызывать, активизировать, запускать',
                                                  'через, на всем протяжении, везде, все время']
        month_day_hour_minute = [[[1, 12, 21, 22],
                                  [2, 21, 11, 22]],
                                 [[1, 1, 14, 6],
                                  [4, 15,  18, 10],
                                  [9, 4, 17, 55],
                                  [12, 11, 21, 21]]]
        year, accesses_count = 2016, []

        def insert_word(engl_word, russian_word, date_time=None):
            en_w = EnglishWord(english=engl_word, russian=russian_word)
            if date_time:
                en_w.date = date_time
            en_w.save()

            st_ = en_w.statistics_set.get(english=en_w.english)
            st_.date = en_w.date
            st_.save()
            return en_w

        for num, english_word in enumerate(self.english_words):
            en_word = None
            m_d_h_m_slice = month_day_hour_minute[num:num + 1][0]
            if m_d_h_m_slice:
                for i, m_d_h_m in enumerate(m_d_h_m_slice):
                    month, day, hour, minute = m_d_h_m[0], m_d_h_m[1], m_d_h_m[2], m_d_h_m[3]
                    date_time = timezone.make_aware(datetime(year, month, day, hour, minute))
                    if i == 0:
                        en_word = insert_word(english_word, self.russian_words[num], date_time)
                    else:
                        st = Statistics(english=en_word, date=date_time)
                        st.save()
            else:
                insert_word(english_word, self.russian_words[num])

    def _test_insert(self):
        english_words = [en_word.english for en_word in EnglishWord.objects.all()]
        self.assertNotEqual(english_words, self.english_words)

        print('uuuuuu')
        print('en-words - ', english_words)
        for num, en_word in enumerate(EnglishWord.objects.all()):
            print(en_word, num, 'zzzzz')
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
