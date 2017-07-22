#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from blog.models import BlogPost


class MomentForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
