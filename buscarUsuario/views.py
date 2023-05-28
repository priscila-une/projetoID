from django.shortcuts import render, get_object_or_404
from .forms import SearchForm
from django.contrib import messages
from django.db.models import Q
from criarConta.models import CustomUser #trocar depois pela tabela dos usuários
from django.contrib.auth import authenticate, login

def buscarUsuario(request):
    form = SearchForm(request.GET or None)
    results = []

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            consulta = form.cleaned_data['consulta']
            request.session['input_value'] = consulta
            results = CustomUser.objects.filter(Q(nome_completo__icontains=consulta) | Q(registro_funcional=consulta))
            results = results.order_by('nome_completo')
            form = SearchForm(initial={'input_field': request.session.get('input_value', '')})

    return render(request, 'buscarUsuario/buscar_usuario.html', {'form': form, 'results': results})

def credencial(request, func_id):
    usuario = get_object_or_404(CustomUser, idfunc=func_id)
    # context: {'registro': registro } permite que o parâmetro seja passado para o template credencial.html
    return render (request, 'credencial/credencial.html', {'usuario': usuario })

def exclui_usuario(request, func_id):
    usuario = get_object_or_404(CustomUser, idfunc=func_id)
    usuario.delete()
    messages.success(request, 'Usuário excluído com sucesso.')
    return render (request, 'buscarUsuario/buscar_usuario.html', {'usuario': usuario })
