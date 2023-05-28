from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from criarConta.models import CustomUser

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():            
            email = form.cleaned_data['email']
            senha = form.cleaned_data["senha"]

            # The authenticate function returns the authenticated user object if the credentials are valid, but it does not handle the creation of the user session. 
            user = authenticate(request, email=email, password=senha)            

            # A função login é responsável por criar a sessão do usuário e requer o objeto user autenticado como argumento.
            if user is not None:
                login(request, user)
                # Guardar user.idfunc na sessão (prefixo: sessao)
                request.session['func_id'] = user.idfunc
                # Acessar o user.idfunc da sessão
                sessao_funcionario_id = request.session.get('func_id')  
                #print(sessao_funcionario_id)            
                return redirect('logado')
            else:
                messages.error(request, 'Email e/ou senha incorretos.')

    else:
        form = LoginForm()
    
    return render(request, 'login/login.html', {'form': form})

def logado(request):
    return render(request, 'buscarUsuario/buscar_usuario.html')
    #return render(request, 'login/login.html')

def deslogado(request):
    logout(request)
    # Redirecionar para uma URL específica após deslogar
    return redirect('/')

