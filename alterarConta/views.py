from django.shortcuts import render, get_object_or_404
from criarConta.models import CustomUser

def alterarConta(request, sessao_funcionario_id):
    funcionario = get_object_or_404(CustomUser, idfunc=sessao_funcionario_id)
    # Guardar os valores na sessão
    request.session['func_id'] = funcionario.idfunc
    request.session['func_nome'] = funcionario.nome_completo
    request.session['func_email'] = funcionario.email

    # Acessar os valores guardados na sessão
    sessao_funcionario_id = request.session.get('func_id')





    return render(request, 'alterarConta/alterar_conta.html', {'funcionario': funcionario })