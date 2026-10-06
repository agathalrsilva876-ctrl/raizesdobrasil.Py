from django.urls import path
from . import views

app_name = 'artesaos'

urlpatterns = [
    path('regioes/', views.regioes, name='regioes'),
    path('cadastrar/', views.cadastrar_artesao, name='cadastrar'),
    path('cadastro-sucesso/', views.cadastro_sucesso, name='cadastro_sucesso'),
]