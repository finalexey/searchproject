# coding=utf8
import requests


def sendrequest(word, top, skip):

    """Функция, отправляющая get запрос по url и возвращающая десериализованный словарь"""

    search_res = requests.get(
        url=f'https://docs.microsoft.com/api/'
            f'search?search={word}&locale=ru-ru&'
            f'scoringprofile=search_for_en_us_a_b_test&'
            f'facet=category&%24skip={skip}&%24top={top}')
    search_res = search_res.json()
    print(search_res)

    return search_res


def search(word, limit):

    """Функция поиска, принимающая аргументами искомое слово и
    количество необходимых результатов в выдаче"""

    results_count = int(limit)
    count = 1
    top = 25
    skip = 0
    top_result = top
    search_result = []
    if results_count > top:
        while top * count <= results_count and top > 0 and top_result <= results_count:
            if results_count - top_result >= top:
                search_result += sendrequest(word, top, skip)['results']
                skip = count * 10
                top_result += top
                count += 1
            else:
                search_result += sendrequest(word, top, skip)['results']
                top = results_count - top_result
                top_result += top
    else:
        top = results_count
        search_result += sendrequest(word, top, skip)['results']

    return search_result
