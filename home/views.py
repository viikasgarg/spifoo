# Create your views here.
from django.shortcuts import render
from django.conf import settings


def home(request, *args, **kwargs):
    url = request.GET.get('url', '')
    site_type = ''
    _url = url.split("//")[-1].split("/")[0]
    if url:
        site_type = settings.DATA.get(_url, "unknown")

    return render(request, "home.html",
                  {'url': url,
                   'site_type': site_type
                   })
