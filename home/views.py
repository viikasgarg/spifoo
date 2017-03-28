# Create your views here.
from django.shortcuts import render
from django.conf import settings


def home(request, *args, **kwargs):
    msg = request.GET.get('msg', '')
    site_type = ''

    if msg:
        site_type = settings.DATA.get(msg, "unknown")

    return render(request, "home.html",
                  {'msg': msg,
                   'site_type': site_type
                   })
