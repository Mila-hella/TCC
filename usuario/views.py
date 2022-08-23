from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>TCC</h1><p>Trabalho de Conclusão </p2<")
