from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from django.template import loader
import praw
from prawcore import NotFound
from prawcore.exceptions import Forbidden
from prawcore.exceptions import BadRequest
from prawcore.exceptions import *
from .forms import NameForm


def sub_exists(sub, reddit):
    exists = True
    try:
        reddit.subreddit(sub)._fetch()
    except:
        exists = False
    return exists


def index(request):
    reddit = praw.Reddit(client_id='bIVav8yQLn_1UQ', client_secret='K1by6B5BddZ5PenhD1hwj-tA1og', user_agent='User')
    name = ''
    form = NameForm(request.POST or None)
    if form.is_valid():
        name = form['sub'].value()

    template = loader.get_template('posts/index.html')
    if name != '' and sub_exists(name, reddit):
        hot_python = reddit.subreddit(name).top(limit=100)
    else:
        hot_python = []

    context = {
        'name': name,
        'form': form,
        'hot_python': hot_python
    }
    return HttpResponse(template.render(context, request))


