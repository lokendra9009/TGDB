from django.http import HttpResponse
import datetime
from django import template
from django.shortcuts import render_to_response
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello Django")


def today_is(request):
    now = datetime.datetime.now()
    # t = template.loader.get_template('blog/datetime.html')
    # c = ({'now': now})
    # html = t.render(c)
    # return HttpResponse(html)
    # return render_to_response('blog/datetime.html', {'now': now})
    return render(request, 'blog/datetime.html', {'now':now, 'template_name': 'blog/nav.html'})
