from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Transaction
from .form import TransactionForm


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


def new_transaction(request):
    data = {}
    form = TransactionForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('url_crud')
    data['form'] = form
    return render(request, 'contas/form.html', data)


def update(request, pk):
    data = {}
    transaction_pk = Transaction.objects.get(pk=pk)
    form = TransactionForm(request.POST or None, instance=transaction_pk)

    if form.is_valid():
            form.save()
            return redirect('url_crud')
    data['form'] = form
    return render(request, 'contas/form.html', data)
