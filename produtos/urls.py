
from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('sul/', views.produtos_sul, name='produtos_sul'),
    path('sudeste/', views.produtos_sudeste, name='produtos_sudeste'),
    path('norte/', views.produtos_norte, name='produtos_norte'),
    path('nordeste/', views.produtos_nordeste, name='produtos_nordeste'),
    path('detalhes/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('cadastrar/<int:artesao_id>/', views.cadastrar_produto, name='cadastrar_produto'),
    path('cadastrado/<int:artesao_id>/', views.produto_cadastrado, name='produto_cadastrado'),

]
