# coding=utf8
from django.http import HttpResponse, JsonResponse
import json

from . import utils


def search_view(request, word, limit):

    search_result = json.dumps(utils.search(word), ensure_ascii=False)

    # return JsonResponse(search_result)
    return HttpResponse(content=search_result,
                        status=200,
                        content_type="application/json")

    # search_result = requests.get(
    #     url=f'https://docs.microsoft.com/api/'
    #         f'search?search={word}&locale=ru-ru&'
    #         f'scoringprofile=search_for_en_us_a_b_test&'
    #         f'facet=category&%24skip=0&%24top=10'
    # )
    # search_result = search_result.json()
    # print('_____________', search_result)
    # title_list = []
    # for single_result in search_result['results']:
    #     if single_result['title']:
    #         title_list.append(single_result['title'])
    #         print(single_result['title'])
    # print(title_list)
    # return HttpResponse(200, search_result)
    # return JsonResponse(search_result)
    # return HttpResponse(simplejson.dumps(search_result), mimetype='application/json')