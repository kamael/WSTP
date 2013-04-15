# -*- coding:utf-8 *-*
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')

def sql_injiection_intro(request):
    return render_to_response('SQL_Injection_intro.html')

def mysql(request):
    return render_to_response('MySQL.html')
#def search(request):
 #   if 'name' in request.GET:
  #      name = request.GET['name']
   #     students = Students.objects.filter(stu_name=name)
    #return render_to_response('name.html',{'students':students})
