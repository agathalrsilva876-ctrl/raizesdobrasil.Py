from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path(
        'cadastrar/<int:artesao_id>/',
        views.cadastrar_produto,
        name='cadastrar'
    ),

    path(
        'cadastrado/<int:artesao_id>/',
        views.produto_cadastrado,
        name='produto_cadastrado'
    ),
]