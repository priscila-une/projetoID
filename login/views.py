from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():            
            email = form.cleaned_data['email']
            senha = form.cleaned_data["senha"]

            # The authenticate function returns the authenticated user object if the credentials are valid, but it does not handle the creation of the user session. 
            user = authenticate(request, email=email, password=senha)            

            # The login function is responsible for creating the user session and requires the authenticated user object as an argument.
            if user is not None:
                login(request, user)
                return redirect('logado')
            else:
                messages.error(request, 'Email e/ou senha incorretos.')

    else:
        form = LoginForm()
    
    return render(request, 'login/login.html', {'form': form})

def logado(request):
    return render(request, 'buscarUsuario/buscar_usuario.html')
