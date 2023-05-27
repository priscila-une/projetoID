from django.shortcuts import render

def alterarConta(request):
    return render(request, 'alterarConta/alterar_conta.html')