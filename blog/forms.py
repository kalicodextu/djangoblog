#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from blog.models import BlogPost
from django import forms


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        # fields = '__all__'
        exclude = ('timestamp',)