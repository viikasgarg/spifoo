# Create your views here.
from django.http import JsonResponse
from django.conf import settings


def home(request, *args, **kwargs):
    data = settings.DATA['100percentfedup.com']
    return JsonResponse(
        {'data': "{}".format(data)})
