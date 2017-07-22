# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import BlogPost


class MomentAdmin(admin.ModelAdmin):
    fieldsets = (
        ("消息内容", {
                'fields': ('title', 'body', 'timestamp')
        }),
        ("用户消息", {
                'fields': ('author',),
        }),
    )


admin.site.register(BlogPost, MomentAdmin)
