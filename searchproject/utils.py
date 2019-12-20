# coding=utf8
import requests
from rest_framework.utils import json


# def search(word):
#     search_result = requests.get(
#         url=f'https://docs.microsoft.com/api/'
#             f'search?search={word}&locale=ru-ru&'
#             f'scoringprofile=search_for_en_us_a_b_test&'
#             f'facet=category&%24skip=0&%24top=10')
#     search_result = search_result.json()
#     print(search_result)
#     return search_result

def search(word):
    results_count = 50
    count = 0
    top = 25
    skip = 0
    search_result = []
    while top*count < results_count:
        search_res = requests.get(
            url=f'https://docs.microsoft.com/api/'
            f'search?search={word}&locale=ru-ru&'
            f'scoringprofile=search_for_en_us_a_b_test&'
            f'facet=category&%24skip={skip}&%24top={top}')
        search_res = search_res.json()          #
        search_result += search_res['results']

        skip += 10
        count += 1
    return search_result
