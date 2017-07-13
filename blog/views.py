# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from blog.forms import MomentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def moments_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse("blog.views.welcome"))
    else:
        form = MomentForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request,
                  os.path.join(PROJECT_ROOT, 'blog/templates',
                               'moments_inputs.html'), {'form': form})

def welcome(request):
    return HttpResponse('<h1>Welcome to kalicodextu blog!</h1>')