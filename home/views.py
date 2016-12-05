# Create your views here.
from django.shortcuts import render
from django.conf import settings


def home(request, *args, **kwargs):
    url = request.GET.get('url', '')
    url = url.split("//")[-1].split("/")[0]
    site_type = settings.DATA.get(url, "don't know")
    return render(request, "home.html",
                  {'url': url,
                   'site_type': site_type
                   })
