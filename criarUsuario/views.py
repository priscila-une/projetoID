from django.shortcuts import render

def criarUsuario(request):
    return render(request, 'criarUsuario/passo1_dadospessoais.html')