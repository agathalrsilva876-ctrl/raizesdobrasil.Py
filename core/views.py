from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')


def quem_somos(request):
    return render(request, 'core/quem_somos.html')

def sudeste(request):
    return render(request, 'core/sudeste.html')
