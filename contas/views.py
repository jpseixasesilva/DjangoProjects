from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Transaction


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def welcome(request):
    data = {}
    data['date_now'] = datetime.datetime.now()
    data['Transaction'] = ['T1add','T2add','T3add']
    return render(request,'contas/welcome.html',data)

def crud(request):
    data = {}
    data['Transaction'] = Transaction.objects.all()
    return render(request, 'contas/crud.html', data)
