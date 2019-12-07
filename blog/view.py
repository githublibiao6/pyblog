# from django.http import HttpResponse
#
#
# def hello(request):
#     return HttpResponse("Hello world ! ")
#  view.py
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'mode/hello.html', context)