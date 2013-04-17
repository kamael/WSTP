# -*- coding:utf-8 *-*
from django.db import models

class TYPE(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
 #   link = models.TextField()
    info  = models.TextField()


class s_type(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    info  = models.TextField() 
    father = models.ForeignKey(TYPE)

class Content(models.Model):
     id = models.AutoField(primary_key = True)
     name = models.CharField(max_length = 50)
     father = models.ForeignKey(s_type)
     source = models.TextField()
     help = models.TextField()
     link = models.TextField()