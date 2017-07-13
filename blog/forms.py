#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from blog.models import Moment


class MomentForm(ModelForm):
    class Meta:
        model = Moment
        fields = '__all__'
