from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('sudeste/', views.sudeste, name='sudeste'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/artesao/', views.dashboard_artesao, name='dashboard_artesao'),
    path('dashboard/artesao/produtos/', views.meus_produtos, name='meus_produtos'),
]