# -*- coding: utf-8 -*-
from models import TYPE, Content, Students
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.utils.translation import ugettext_lazy as _
from forms import RegisterForm, LoginForm
import datetime


def online_time(user):
    onlinetime = 0
    onlinedays = 0
    onlinehours = 0
    onlineminutes = 0
    try:
        onlinedays = int(datetime.datetime.now().strftime("%d")) - int(user.date_joined.strftime("%d"))
        onlinehours = int(datetime.datetime.now().strftime("%H")) - int(user.date_joined.strftime("%H"))-8
        onlineminutes = int(datetime.datetime.now().strftime("%M")) - int(user.date_joined.strftime("%M"))
        if onlineminutes < 0:
            onlineminutes += 60
            onlinehours -= 1
        if onlinehours < 0:
            onlinehours += 24
            onlinedays -= 1
        onlinetime = [onlinedays, onlinehours, onlineminutes]
    except:
        onlinetime = [0, 0, 0]
    return onlinetime


def add_grades(username, q):  # request.user()
    user = User.objects.get(username=username)
    if user.grades is None:
        user.grades = 0
    user.grades = int(user.grades) + int(q.grade)
    user.questions = str(user.questions) + str(q.id) + ';'
    user.answers = str(user.answers)+str(q.answer)+';'
    user.commit_time = datetime.datetime.now()
    user.save()


def update_name(username, name):
    user = User.objects.get(username=username)
    user.first_name = name
    user.save()


def myrank(username):
    count = 1
    user = User.objects.order_by('-grades', 'commit_time')
    for i in user:
        if username == i.username:
            break
        else:
            count += 1
    return count


def check_answer(request, offset):
    if request.user.is_authenticated():  # 判断用户是否已登录
        try:
            q = Content.objects.get(id=offset)
            if q.answer == request.POST['password'].strip() and offset not in User.objects.get(username=request.user).questions.split(';'):
                add_grades(request.user, q)
        except:
            pass
        return HttpResponseRedirect('/content/'+str(offset))


def index(request):
    Type = TYPE.objects.all()
    content = Content.objects.all()
    ncontent = []
    userrank = User.objects.order_by('-grades', 'commit_time')[:10]
    for i in Type:
        ncontent.append(0)
        for j in content:
            if i.id == j.father_id:
                ncontent[j.father_id-1] += 1
    ncontent.reverse()
    time = [0, 0, 0]
    rank = ' - '

    if request.user.is_authenticated():  # 判断用户是否已登录
            user = User.objects.get(username=request.user)
            time = online_time(User.objects.get(username=request.user))
            rank = myrank(user.username)
    else:
        user = ''

    return render_to_response('index.html',
                              {'Types': Type,
                              'contents': content,
                              'numofcontents': ncontent,
                              'user': user,
                              'time': time,
                              'userrank': userrank,
                              'rank': rank},
                              context_instance=RequestContext(request))


def content(request, offset):
    Type = TYPE.objects.all()
    content = Content.objects.all()
    contentneed = Content.objects.get(id=offset)
    Typeneed = TYPE.objects.get(id=contentneed.father_id)
    ncontent = []
    for i in Type:
        ncontent.append(0)
        for j in content:
            if i.id == j.father_id:
                ncontent[j.father_id-1] += 1
    ncontent.reverse()
    time = [0, 0, 0]
    if request.user.is_authenticated():  # 判断用户是否已登录
        user = User.objects.get(username=request.user)
        time = online_time(User.objects.get(username=request.user))
        try:
            q = user.questions.split(';')
            questions = []
            for i in q:
                if i:
                    questions.append(int(i))
        except:
            questions = []
    else:
        user = ''
        questions = []

    return render_to_response('content.html',
                              {'Types': Type,
                              'Typeneed': Typeneed,
                              'contents': content,
                              'numofcontents': ncontent,
                              'contentneeds': contentneed,
                              'user': user,
                              'questions': questions,
                              'time': time},
                              context_instance=RequestContext(request))


def register(request):
    '''注册视图'''
    # template_var = {}
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST.copy())
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username, '', password)
            user.tel = request.POST['tel']
            user.grades = 0
            user.save()
            try:
                update_name(username, Students.objects.get(card=username).stu_name)
            except:
                pass
            _login(request, username, password)  # 注册完毕 直接登陆
    return HttpResponseRedirect('/')


def login(request):
    '''登陆视图'''
    # template_var = {}
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST.copy())
        if form.is_valid():
            _login(request, form.cleaned_data["username"], form.cleaned_data["password"])
    return HttpResponseRedirect('/')


def _login(request, username, password):
    '''登陆核心方法'''
    ret = False
    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            auth_login(request, user)
            ret = True
    else:
        messages.add_message(request, messages.INFO, _(u'用户不存在'))
    return ret


def logout(request):
    '''注销视图'''
    auth_logout(request)
    return HttpResponseRedirect('/')


#相应jquery ajax请求
def check_username(request):
    response_str = "false"
    if request.method == 'GET':
        try:
            user = User.objects.get(username=request.GET['username'])
            if user is not None:
                response_str = "false"
        except:
            response_str = "true"
    return HttpResponse("%s" % response_str)


def check_tel(request):
    response_str = "false"
    if request.method == 'GET':
        try:
            user = User.objects.get(tel=request.GET['tel'])
            if user is not None:
                response_str = "false"
        except:
            response_str = "true"
    return HttpResponse("%s" % response_str)
