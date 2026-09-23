from django.urls import path
from . import views

app_name = 'artesaos'

urlpatterns = [
    path('regioes/', views.regioes, name='regioes'),
]