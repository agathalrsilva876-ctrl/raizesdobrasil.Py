from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
]