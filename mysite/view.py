from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template

def index(request):
    content = {"hello","hi","fine"}
    context = {'content':content,}
    return render(request, 'index.html', context)

def table(request):

    return render(request,'tables.html')


