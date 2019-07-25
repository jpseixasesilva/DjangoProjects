from django.shortcuts import render
from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def welcome(request):
    data = {}
    data['date_now'] = datetime.datetime.now()
    data['Transaction'] = ['T1','T2','T3']
    return render(request, 'contas/welcome.html', data)
