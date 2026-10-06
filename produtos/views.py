from django.shortcuts import render
from .models import Produto


def produtos_sul(request):
    produtos = Produto.objects.filter(regiao='Sul')
    return render(request, 'produtos/sul.html', {'produtos': produtos})