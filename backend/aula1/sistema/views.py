from django.shortcuts import render

# Aqui irão ficar todas a views (controladores) ref ao sistema
# A funçao index informa o que vai ser exibido na tela

def index(request):
    return render(
        request, 
        'sistema/sistema.html',
        )


def apresentacao(request):
    return render(
        request, 
        'sistema/apresentacao.html',
        )
