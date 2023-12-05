from django.http import HttpResponse
from django.shortcuts import render


def frontpage(request):
    return HttpResponse('Привет мир!')


def contacts(request):
    return HttpResponse('<h1>Контакты</h1>')
