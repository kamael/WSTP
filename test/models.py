# -*- coding:utf-8 *-*
from django.db import models

class TYPE(models.Model):
    name = models.CharField(max_length = 50)
 #   link = models.TextField()
    info  = models.TextField()


class s_type(models.Model):
    name = models.CharField(max_length = 50)
    info  = models.TextField() 
    father = models.ForeignKey(TYPE)
    content = models.TextField()

