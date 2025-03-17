from django.shortcuts import render

# CAqui irão ficar todas a views (controladores) ref ao sistema

def index(request):
    return render(
        request, 
        'sistema/index.html',
        )


