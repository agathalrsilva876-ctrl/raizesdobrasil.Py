
from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('sul/', views.produtos_sul, name='produtos_sul'),
    path('sudeste/', views.produtos_sudeste, name='produtos_sudeste'),
    path(
        'detalhes/<int:produto_id>/',
        views.detalhes_produto,
        name='detalhes_produto'
    ),
]
