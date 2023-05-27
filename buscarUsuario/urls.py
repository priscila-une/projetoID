from django.urls import path
from buscarUsuario.views import buscarUsuario

urlpatterns = [
    path('pesquisa', buscarUsuario, name='pesquisa'),
    path('buscarUsuario/', buscarUsuario, name='buscar_usuario'),
]