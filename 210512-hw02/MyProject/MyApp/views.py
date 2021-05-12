from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1><font color = 'red'>오늘은 수요일</font></h1>")