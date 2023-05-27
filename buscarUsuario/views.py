from django.shortcuts import render
from .forms import SearchForm
from criarConta.models import CustomUser #trocar depois pela tabela dos usuários

def buscarUsuario(request):
    form = SearchForm(request.GET or None)
    results = []

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            consulta = form.cleaned_data['consulta']
            results = CustomUser.objects.filter(nome_completo__icontains=consulta)

    return render(request, 'buscarUsuario/buscar_usuario.html', {'form': form, 'results': results})
