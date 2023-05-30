from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, CustomUser
from buscarUsuario.views import buscarUsuario
from django.contrib import messages
from django.utils import timezone
from datetime import datetime

def passo1(request):
    if request.method == 'POST':
        # Recuperar dados do formulário (Passo 1)
        form_passo1 = request.POST.dict()
        # Criar variáveis de sessão
        request.session.update(form_passo1)
        # Armazenar os valores coletados do formulário (Passo 1) em sessões de variáveis 
        request.session['numero_cadastro'] = form_passo1['numero_cadastro']
        request.session['eol'] = form_passo1['eol']
        request.session['nome_completo'] = form_passo1['nome_completo']
        request.session['nome_social'] = form_passo1['nome_social']
        request.session['raca_cor'] = form_passo1['raca_cor']
        request.session['cidade'] = form_passo1['cidade']
        request.session['uf'] = form_passo1['uf']

        # Formatação do campo 'date' de data_nascimento
        data_nascimento_str = form_passo1['data_nascimento']
        data_nascimento = datetime.strptime(data_nascimento_str,'%Y-%m-%d')
        data_nascimento_formatado = data_nascimento.strftime('%Y-%m-%d')  
        request.session['data_nascimento'] = data_nascimento_formatado # Atribuir a data formatada à variável de sessão

        request.session['idade'] = form_passo1['idade']
        request.session['certidao_nascimento'] = form_passo1['certidao_nascimento']
        request.session['folha'] = form_passo1['folha']
        request.session['livro'] = form_passo1['livro']
        request.session['numero_certidao'] = form_passo1['numero_certidao']
        request.session['rg'] = form_passo1['rg']

        # Formatação do campo 'date' de data_expedicao
        data_expedicao_str = form_passo1['data_expedicao']
        data_expedicao = datetime.strptime(data_expedicao_str,'%Y-%m-%d')
        data_expedicao_formatado = data_expedicao.strftime('%Y-%m-%d')  
        request.session['data_expedicao'] = data_expedicao_formatado # Atribuir a data formatada à variável de sessão

        request.session['necessidade_especial'] = form_passo1['necessidade_especial']                        
        request.session['nome_completo_responsavel'] = form_passo1['nome_completo_responsavel']

        # Redirecionar para o formulário -> Passo 2
        return redirect('passo_dois')
    else:
        return render(request,'criarUsuario/passo1_dadospessoais.html')

def passo2(request):
    if request.method == 'POST':
        # Recuperar dados do formulário (Passo 2)
        form_passo2 = request.POST.dict()
        # Criar variáveis de sessão
        request.session.update(form_passo2)
        # Armazenar os valores coletados do formulário (Passo 2) em sessões de variáveis
        request.session['endereco'] = form_passo2['endereco']
        request.session['endereco_numero'] = form_passo2['endereco_numero']
        request.session['complemento'] = form_passo2['complemento']
        request.session['cep'] = form_passo2['cep']
        request.session['telefone_residencial'] = form_passo2['telefone_residencial']
        request.session['telefone_celular'] = form_passo2['telefone_celular']
        request.session['telefone_recado'] = form_passo2['telefone_recado']
        request.session['nome_telefone_recado'] = form_passo2['nome_telefone_recado']              
        # Redirecionar para o formulário -> Passo 3
        return redirect('passo_tres')
    else:
        return render(request,'criarUsuario/passo2_endereco.html')

def passo3(request):
    if request.method== 'POST':
        # Recuperar dados do formulário (Passo 3)
        form_passo3 = request.POST.dict()
        # Criar variáveis de sessão
        request.session.update(form_passo3)
       # Armazenar os valores coletados do formulário (Passo 3) em sessões de variáveis
        request.session['tipo_sanguineo'] = form_passo3['tipo_sanguineo']
        request.session['convenio'] = form_passo3['convenio']
        request.session['alergias'] = form_passo3['alergias']
        request.session['problemas_saude'] = form_passo3['problemas_saude']
        request.session['tratamento_medico'] = form_passo3['tratamento_medico']
        request.session['restricao_ativfisica'] = form_passo3['restricao_ativfisica']
        request.session['lesao_fratura_cirurgia'] = form_passo3['lesao_fratura_cirurgia']                                            
        # Redirecionar para o formulário -> Passo 4
        return redirect('passo_quatro')
    else:
        return render(request,'criarUsuario/passo3_dadosmedicos.html')

def passo4(request):
    if request.method == 'POST':

       # id do funcionário que está logado (chave estrangeira)
        func_id = request.session['sessao_func_id'] 
        funcionario = CustomUser.objects.get(idfunc=func_id)

        # Salvar os dados da sessão na base de dados
        dados_do_usuario = Usuario(
            #----- Passo 1 -----#
            idfunc = funcionario, 
            numero_cadastro = request.session['numero_cadastro'],
            eol = request.session['eol'],
            nome_completo = request.session['nome_completo'],
            nome_social = request.session['nome_social'],
            raca_cor = request.session['raca_cor'],
            cidade = request.session['cidade'],
            uf = request.session['uf'],
            data_nascimento = request.session['data_nascimento'],
            idade = request.session['idade'],
            certidao_nascimento = request.session['certidao_nascimento'],
            folha = request.session['folha'],
            livro = request.session['livro'],
            numero_certidao = request.session['numero_certidao'],
            rg = request.session['rg'],
            data_expedicao = request.session['data_expedicao'],
            necessidade_especial = request.session['necessidade_especial'],
            nome_completo_responsavel = request.session['nome_completo_responsavel'],
            #----- Passo 2 -----# 
            endereco = request.session['endereco'], 
            endereco_numero = request.session['endereco_numero'],
            complemento = request.session['complemento'],
            cep = request.session['cep'],
            telefone_residencial = request.session['telefone_residencial'],
            telefone_celular = request.session['telefone_celular'],
            telefone_recado = request.session['telefone_recado'],
            nome_telefone_recado = request.session['nome_telefone_recado'], 
            #----- Passo 3 -----#
            tipo_sanguineo = request.session['tipo_sanguineo'], 
            convenio = request.session['convenio'], 
            alergias = request.session['alergias'],
            problemas_saude = request.session['problemas_saude'],
            tratamento_medico = request.session['tratamento_medico'],
            restricao_ativfisica = request.session['restricao_ativfisica'],
            lesao_fratura_cirurgia = request.session['lesao_fratura_cirurgia']            
        )
        dados_do_usuario.save()

        #----- Apagar o conteúdo das variáveis de sessão, exceto as do funcionário logado -----#
        # Identificar quais são as variáveis de sessão relacionadas ao funcionário logado
        variaveis_sessao_funcionario = ['email', 'password', 'sessao_func_id']

        # Iterar sobre as variáveis de sessão
        for key in list(request.session.keys()):
            if key not in variaveis_sessao_funcionario:
                del request.session[key]

        # Salvar a modificação da sessão
        request.session.modified = True

        #foto3x4
        #rg_usuario
        #cert_nasc_usuario
        #rg_responsavel
        #comprov_residencia
        #autorizacao

        messages.success(request, "O usuário foi cadastrado com sucesso!") 
        return render (request,'criarUsuario/passo1_dadospessoais.html')

    else:
        return render (request,'criarUsuario/passo4_enviardocumentos.html')