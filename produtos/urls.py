from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('norte/', views.produtos_norte, name='produtos_norte'),

    path('centro-oeste/', views.produtos_centro_oeste, name='produtos_centro_oeste'),

    path('sul/', views.produtos_sul, name='produtos_sul'),

    path('sudeste/', views.produtos_sudeste, name='produtos_sudeste'),

    path(
        'detalhes/<int:produto_id>/',
        views.detalhes_produto,
        name='detalhes_produto'
    ),
]