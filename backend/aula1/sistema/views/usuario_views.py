from django.shortcuts import render

from sistema.models import Usuario

def listarUsuario(request):
    usuarios = Usuario.objects.all()

    context = {
        'usuarios': usuarios,
    }

    return render(
        request, 
        'usuarios/listar.html',
        context,
        )