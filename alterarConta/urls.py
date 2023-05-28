from django.urls import path
from alterarConta.views import alterarConta

urlpatterns = [
    path('alterarConta/', alterarConta, name='alterar_conta'),
    path('alterarConta/<int:sessao_funcionario_id>/', alterarConta, name='alterar_cadastro'),
]