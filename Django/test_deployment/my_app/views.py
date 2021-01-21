from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('This is the landing page')


def help(request):
    return HttpResponse('This is the help page')
