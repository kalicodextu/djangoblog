# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from blog.models import BlogPost
from django.template import loader, Context, RequestContext
from datetime import datetime
from .forms import BlogPostForm

# Create your views here.

# def moments_input(request):
#     if request.method == 'POST':
#         form = MomentForm(request.POST)
#         if form.is_valid():
#             moment = form.save()
#             moment.save()
#             return HttpResponseRedirect(reverse("blog.views.welcome"))
#     else:
#         form = MomentForm()
#     PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     return render(request,
#                   os.path.join(PROJECT_ROOT, 'blog/templates',
#                                'moments_inputs.html'), {'form': form})


def welcome(request):
    return HttpResponse('<h1>Welcome to kalicodextu blog!</h1>')


def archive(request):
    posts = BlogPost.objects.all().order_by('-timestamp')
    # t = loader.get_template("archive.html")
    # c = Context().update({'posts': posts})
    # return HttpResponse(t.render(c))
    return render(request, 'archive.html', {'posts': posts,'form':BlogPostForm()})


# archive = lambda req: render_to_response('archive.html', {'posts': BlogPost.objects.all()})


def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            body=request.POST.get('body'),
            timestamp=datetime.now(),
            ).save()
    return HttpResponseRedirect('/blog/view')
