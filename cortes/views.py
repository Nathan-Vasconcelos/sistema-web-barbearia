from django.shortcuts import render

from cortes.models import Corte

# Create your views here.
def index(request):
    return render(request, 'index.html')


def cabelo(request):
    cortes = Corte.objects.filter(categoria='cabelo')
    #cortes = Corte.objects.all()

    dados = {
        'cortes' : cortes
    }
    return render(request, 'cabelo.html', dados)


def barba(request):
    cortes = Corte.objects.filter(categoria='barba')

    dados = {
        'cortes' : cortes
    }

    return render(request, 'barba.html', dados)


def informacoes(request):
    return render(request, 'informacoes.html')
