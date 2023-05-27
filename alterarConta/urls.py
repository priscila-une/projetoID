from django.urls import path
from alterarConta.views import alterarConta

urlpatterns = [
    path('alterarConta/', alterarConta, name='alterar_conta'),
]