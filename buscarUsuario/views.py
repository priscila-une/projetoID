from django.shortcuts import render, get_object_or_404
from .forms import SearchForm
from django.contrib import messages
from django.db.models import Q
from criarConta.models import CustomUser #trocar depois pela tabela dos usuários
from criarUsuario.models import Usuario
from django.contrib.auth import authenticate, login

def buscarUsuario(request):
    form = SearchForm(request.GET or None)
    results = []

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            consulta = form.cleaned_data['consulta']            
            #results = Usuario.objects.filter(Q(nome_completo__icontains=consulta) | Q(eol=consulta))

            # Try converting the search term to an integer
            try:
                eol_consulta = int(consulta)
                results = Usuario.objects.filter(Q(nome_completo__icontains=consulta) | Q(eol=eol_consulta))
            except ValueError:
                # Handle the case when the search term cannot be converted to an integer
                results = Usuario.objects.filter(Q(nome_completo__icontains=consulta) | Q(nome_completo__icontains=str(consulta)))

            results = results.order_by('nome_completo')

    return render(request, 'buscarUsuario/buscar_usuario.html', {'form': form, 'results': results})

def credencial(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    return render (request, 'credencial/credencial.html', {'usuario': usuario })

def exclui_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    usuario.delete()
    messages.success(request, 'Usuário excluído com sucesso.')
    return render (request, 'buscarUsuario/buscar_usuario.html', {'usuario': usuario })
