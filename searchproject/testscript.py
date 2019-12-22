import unittest

from searchproject.searchproject import utils


class SearchTest(unittest.TestCase):

    def test_search(self, word='linq', limit=50):

        """Функция проверяет вхождение искомого слова в заголовки выдачи результатов поиска,
        при отсутствии вхождения выбрасывает AssertionError"""

        result_list = utils.search(word=word, limit=limit)

        for single_dict in result_list:
            if single_dict['title']:
                self.assertIn(word, single_dict['title'].lower(), msg='Word not found')


if __name__ == '__main__':
    unittest.main()
