from django.shortcuts import render
from django.http import HttpResponse


def list_stocks(request):
    return HttpResponse('rota para listar os ativos cadastrados')
