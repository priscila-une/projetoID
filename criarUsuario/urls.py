from django.urls import path
from criarUsuario.views import criarUsuario

urlpatterns = [
    path('criarUsuario/', criarUsuario, name='criar_usuario'),
]