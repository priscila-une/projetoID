from django.urls import path
from .views import signin, logado, deslogado

urlpatterns = [
    path('', signin, name='login_funcionario'), #name = nome da path para indicar em outra página que eu vou clicar e ir para essa página
    path('buscarUsuario/', logado, name='logado'),
    path('sair/', deslogado, name='sair'),
]