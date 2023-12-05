from django.http import HttpResponse
from django.shortcuts import render


def frontpage(request):
    return HttpResponse('Привет мир!')


def contact(request):
    return HttpResponse('Привет мир!')
