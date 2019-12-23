from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.template import Template
from polls.models import Choice,Question
from django.apps import apps

def get_model_field(app_name,model_name):  #获取 数据库表字段的原始名字 和 verbose_name
    model_obj = apps.get_model(app_name,model_name)
    field_dic={}
    for field in model_obj._meta.fields:
        field_dic[field.name] = field.verbose_name
    return field_dic

def index(request):
    content = {"hello","hi","fine"}
    context = {'content':content,}
    return render(request, 'index.html', context)

def tables(request):
    question_list = Question.objects.all()
    question_attr = get_model_field('polls','Question')
    print(question_attr)
    print(question_list)
    context = {'question_list':question_list,'question_attr':question_attr}
    return render(request,'tables.html',context)


