# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Moment


class MomentAdmin(admin.ModelAdmin):
    fieldsets = (
        ("消息内容", {
                'fields': ('content', 'kind')
        }),
        ("用户消息", {
                'fields': ('user_name',),
        }),
    )


admin.site.register(Moment, MomentAdmin)
