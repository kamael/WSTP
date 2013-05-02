# -*- coding:utf-8 *-*
from models import TYPE,s_type,Content,Students
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest 
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from django.utils.translation import ugettext_lazy as _
from forms import RegisterForm,LoginForm,AjaxForm
from django.utils import simplejson

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
    stu = ''
    if request.user.is_authenticated():     #判断用户是否已登录
        user = request.user          #获取已登录的用户
        try:
            stu = Students.objects.filter( card = user)[0].stu_name
        except:
            stu = ''
    else:   
        user = ''

    return render_to_response('index.html',{
        'Types':Type,
        's_Types':s_Type,
        'numofs_Types':ns_Type,
        'contents':content,
        'user':user,
        'stu':stu

        },context_instance=RequestContext(request))

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
    stu = ''
    if request.user.is_authenticated():     #判断用户是否已登录
        user = request.user          #获取已登录的用户
        try:
            stu = Students.objects.filter( card = user)[0].stu_name
        except:
            stu = ''
    else:   
        user = ''
    return render_to_response('intro.html',{
        'Types':Type,
        's_Types':s_Type,
        'numofs_Types':ns_Type,
        'Typeneeds':Typeneed,
        'contents':content,
        'user':user,
        'stu':stu
        },context_instance=RequestContext(request))

def content_default(request,offset):
    s_Type = s_type.objects.filter(name=offset)
    Type = TYPE.objects.filter(id=s_Type[0].father_id)
    content = Content.objects.filter(father_id=s_Type[0].id)
    stu = ''
    if request.user.is_authenticated():     #判断用户是否已登录
        user = request.user          #获取已登录的用户
        try:
            stu = Students.objects.filter( card = user)[0].stu_name
        except:
            stu = ''
    else:   
        user = ''
    return render_to_response('content_default.html',{
        'Types':Type,
        's_Types':s_Type,
        'contents':content,
        'user':user,
        'stu':stu
        },context_instance=RequestContext(request))

def content(request,offset1,offset2):
    s_Type = s_type.objects.filter(name=offset1)
    Type = TYPE.objects.filter(id=s_Type[0].father_id)
    content = Content.objects.filter(father_id=s_Type[0].id)
    contentneed =Content.objects.filter(name=offset2)
    stu = ''
    if request.user.is_authenticated():     #判断用户是否已登录
        user = request.user          #获取已登录的用户
        try:
            stu = Students.objects.filter( card = user)[0].stu_name
        except:
            stu = ''
    else:   
        user = ''
    return render_to_response('content.html',{
        'Types':Type,
        's_Types':s_Type,
        'contents':content,
        'contentneeds':contentneed,
        'user':user,
        'stu':stu
        },context_instance=RequestContext(request))




def register(request):
    '''注册视图'''
    template_var={}
    form = RegisterForm()    
    if request.method=="POST":
        form=RegisterForm(request.POST.copy())
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=User.objects.create_user(username,email,password)
            user.save()
            _login(request,username,password)#注册完毕 直接登陆
    return index(request)
    
def login(request):
    '''登陆视图'''
    template_var={}
    form = LoginForm()    
    if request.method == 'POST':
        form=LoginForm(request.POST.copy())
        if form.is_valid():
            _login(request,form.cleaned_data["username"],form.cleaned_data["password"])
    return index(request)  
    
def _login(request,username,password):
    '''登陆核心方法'''
    ret=False
    user=authenticate(username=username,password=password)
    if user:
        if user.is_active:
            auth_login(request,user)
            ret=True
    else:
        messages.add_message(request, messages.INFO, _(u'用户不存在'))
    return ret
    
def logout(request):
    '''注销视图'''
    auth_logout(request)
    return index(request)    


#相应jquery ajax请求  
def check_username(request):  
    response_str = "false"
    if request.method == 'GET':  
        try:  
            user = User.objects.get(username = request.GET['username'])  
            if user is not None:  
                response_str = "false"
        except:
            response_str = "true"
    return HttpResponse("%s" % response_str)

def check_email(request):  
    response_str = "false"
    if request.method == 'GET':  
        try:  
            user = User.objects.get(email = request.GET['email'])  
            if user is not None:  
                response_str = "false"
        except:
            response_str = "true"
    return HttpResponse("%s" % response_str)