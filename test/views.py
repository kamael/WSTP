# -*- coding:utf-8 *-*
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import TYPE,s_type,Content

def index(request):
    Type = TYPE.objects.all()
    s_Type = s_type.objects.all()
    ns_Type=[]
    for i in Type:
        ns_Type.append(0)
        for j in s_Type:
            if i.id == j.father_id:
                ns_Type[j.father_id-1]+=1

    ns_Type.reverse()
    return render_to_response('index.html',{
        'Types':Type,
        's_Types':s_Type,
        'numofs_Types':ns_Type,
        'contents':content
        })

def intro(request,offset):
    Type = TYPE.objects.all()
    Typeneed = TYPE.objects.filter(name=offset)
    s_Type = s_type.objects.all()
    content = Content.objects.all()
    ns_Type=[]
    for i in Type:
        ns_Type.append(0)
        for j in s_Type:
            if i.id == j.father_id:
                ns_Type[j.father_id-1]+=1

    ns_Type.reverse()
    return render_to_response('intro.html',{
        'Types':Type,
        's_Types':s_Type,
        'numofs_Types':ns_Type,
        'Typeneeds':Typeneed,
        'contents':content
        })

def content_default(request,offset):
    s_Type = s_type.objects.filter(name=offset)
    Type = TYPE.objects.filter(id=s_Type[0].father_id)
    content = Content.objects.filter(father_id=s_Type[0].id)
    return render_to_response('content_default.html',{
        'Types':Type,
        's_Types':s_Type,
        'contents':content
        })

def content(request,offset1,offset2):
    s_Type = s_type.objects.filter(name=offset1)
    Type = TYPE.objects.filter(id=s_Type[0].father_id)
    content = Content.objects.filter(father_id=s_Type[0].id)
    contentneed =Content.objects.filter(name=offset2)
    return render_to_response('content.html',{
        'Types':Type,
        's_Types':s_Type,
        'contents':content,
        'contentneeds':contentneed
        })

#def search(request):
 #   if 'name' in request.GET:
  #      name = request.GET['name']
   #     students = Students.objects.filter(stu_name=name)
    #return render_to_response('name.html',{'students':students})
