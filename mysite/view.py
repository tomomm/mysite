from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    content = {"hello","hi","fine"}
    context = {'content':content}
    return render(request, 'index.html', context)
