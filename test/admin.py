# -*- coding: utf-8 -*-
from django.contrib import admin
from test.models import TYPE, Content


class TYPEAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    def __unicode__(self):
        return self.name


class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'father', 'link', 'answer', 'grade')

    def __unicode__(self):
        return self.name


admin.site.register(TYPE, TYPEAdmin)
admin.site.register(Content, ContentAdmin)
