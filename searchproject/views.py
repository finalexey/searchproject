# coding=utf8
from django.http import HttpResponse
import json

from . import utils


def search_view(request, word, limit):

    search_result = json.dumps(utils.search(word, limit), ensure_ascii=False)

    return HttpResponse(content=search_result,
                        status=200,
                        content_type="application/json")
