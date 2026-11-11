from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('norte/', views.produtos_norte, name='produtos_norte'),
    path('nordeste/', views.produtos_nordeste, name='produtos_nordeste'),
    path('sul/', views.produtos_sul, name='produtos_sul'),
    path('sudeste/', views.produtos_sudeste, name='produtos_sudeste'),
    path('centro-oeste/', views.produtos_centro_oeste, name='centro_oeste'),

    path('cadastrar/<int:artesao_id>/', views.cadastrar_produto, name='cadastrar_produto'),
    path('cadastro-sucesso/<int:artesao_id>/', views.produto_cadastrado, name='produto_cadastrado'),

    path(
        'cadastrar/<int:artesao_id>/',
        views.cadastrar_produto,
        name='cadastrar'
    ),
    ]