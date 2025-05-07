from django.shortcuts import render, redirect  

from filmes.forms import FilmeForm       

def listagem(request):
    return render(
        request,           # Requisição HTTP
        'listagem.html'       # Template a ser exibido
    )

# View para cadastrar um novo usuário
def criarFilme(request):
    
    if request.method == 'POST':
        # Cria um formulário com os dados enviados (texto e imagem)
        form = FilmeForm(request.POST)

        

        if form.is_valid():     # Verifica se os dados são válidos
            form.save()         # Salva o novo usuário no banco de dados
            return redirect('/filme/listagem')  # Redireciona para a tela de login após o cadastro

    else:
        # Se a requisição for GET, ou seja, só para exibir a página
        form = FilmeForm()    # Cria um formulário em branco

    # Renderiza o formulário na página de cadastro
    return render(
        request,                # Requisição recebida
        'cadastrar.html',        # Página HTML a ser exibida
        {'form': form}          # Envia o formulário para o template
    )