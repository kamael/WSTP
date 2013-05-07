# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class TYPE(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    #link = models.TextField()
    info = models.TextField()


class s_type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    info = models.TextField()
    father = models.ForeignKey(TYPE)


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    father = models.ForeignKey(TYPE)
    source = models.TextField()
    help = models.TextField()
    link = models.TextField()
    answer = models.TextField()
    grade = models.IntegerField()


class Students(models.Model):
    stu_name = models.CharField(max_length=20)
    stu_college = models.CharField(max_length=60)
    stu_major = models.CharField(max_length=60)
    student_id = models.CharField(max_length=30)
    card = models.CharField(max_length=30)


class ProfileBase(type):
    def __new__(cls, name, bases, attrs):
        #module = attrs.pop('__module__')
        parents = [b for b in bases if isinstance(b, ProfileBase)]
        if parents:
            fields = []
            for obj_name, obj in attrs.items():
                if isinstance(obj, models.Field):
                    fields.append(obj_name)
                User.add_to_class(obj_name, obj)
            UserAdmin.fieldsets = list(UserAdmin.fieldsets)
            UserAdmin.fieldsets.append((name, {'fields': fields}))
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)


class Profile(object):
    __metaclass__ = ProfileBase


class MyProfile(Profile):
    grades = models.IntegerField(null=True, blank=True)
    answers = models.TextField()
    questions = models.TextField()
