from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('It is main page')
