# from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. 지니킴스프로젝트에 온걸 환영해.")
