from django.urls import path
from buscarUsuario.views import buscarUsuario, credencial, exclui_usuario

urlpatterns = [
    path('pesquisa', buscarUsuario, name='pesquisa'),
    path('buscarUsuario/', buscarUsuario, name='buscar_usuario'),

    path('credencial/<int:func_id>/', credencial, name='gera_credencial'),
    path('credencial', credencial, name='credencial'),

    path('exclui_usuario/<int:func_id>/', exclui_usuario, name='exclui_usuario'),
]