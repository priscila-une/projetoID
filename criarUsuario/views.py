from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, CustomUser
from buscarUsuario.views import buscarUsuario

# criar uma loogica aonde eu busco os registros do funcionario
# pelo nome que eu incluir no campo de busca e se achar o registro, me retornar na tela.

def passo1(request):
    if request.method == 'POST':
        # Recuperar dados do formulário (Passo 1)
        form_passo1 = request.POST.dict()
        # Criar variáveis de sessão
        request.session.update(form_passo1)
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
        # Redirecionar para o formulário -> Passo 4
        return redirect('passo_quatro')
    else:
        return render(request,'criarUsuario/passo3_dadosmedicos.html')

def passo4(request):

    if request.method == 'POST':
        passo1_dados = request.session.get('passo1_data')
        passo2_dados = request.session.get('passo2_data')
        passo3_dados = request.session.get('passo3_data')

        idfunc = request.session.get('user_id') #recuperando id da sessão

        funcionario = get_object_or_404(Funcionario, idfunc=idfunc)

        dados_completos = {
            'idfunc': funcionario,
            'eol': passo1_dados.get('eol', ''),
            'nome': passo1_dados.get('nome', ''),
            'nomesocial': passo1_dados.get('nomesocial', ''),
            'raca': passo1_dados.get('raca', ''),
            'cidade': passo1_dados.get('cidade', ''),
            'uf': passo1_dados.get('uf', ''),
            'datanasc': passo1_dados.get('datanasc') or None,
            'idade': passo1_dados.get('datanasc', ''),
            'certidao': passo1_dados.get('certidao', ''),
            'folha': passo1_dados.get('folha', ''),
            'livro': passo1_dados.get('livro', ''),
            'rg': passo1_dados.get('rg', ''),
            'dataexp': passo1_dados.get('dataexp') or None,
            'nespecial': passo1_dados.get('nespecial', ''),
            'nomemae': passo1_dados.get('nomemae', ''),
            'endereco': passo2_dados.get('endereco', ''),
            'numendereco': passo2_dados.get('numero', ''),
            'complemento': passo2_dados.get('complemento', ''),
            'cep': passo2_dados.get('cep', ''),
            'tel': passo2_dados.get('tel', ''),
            'celular': passo2_dados.get('celular', ''),
            'telrecado': passo2_dados.get('telrecado', ''),
            'nomerecado': passo2_dados.get('nomerecado', ''),
            'tpsanguineo': passo3_dados.get('tpsanguineo', ''),
            'convenio': passo3_dados.get('convenio', ''),
            'usamedicamento': passo3_dados.get('usamedicamento', ''),
            'possuialergia': passo3_dados.get('possuialergia', ''),
            'restricaoativ': passo3_dados.get('restricao_ativfisica', ''),
            'problemasaude': passo3_dados.get('problemas_saude', ''),
            'possuilesao': passo3_dados.get('lesao_fratura_cirurgia', '')
        }
    
        formulario_completo = Usuario(**dados_completos)
        formulario_completo.save()

        return buscarUsuario(request)

    else:
        return render (request,'criarUsuario/passo4_enviardocumentos.html')