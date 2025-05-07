from django.shortcuts import render, redirect  # Importa funções para exibir páginas e redirecionar

from usuarios.forms import UsuarioForm        # Importa o formulário baseado no model Usuario

# View para exibir a tela de login
def login(request):
    return render(
        request,           # Requisição HTTP
        'login.html'       # Template a ser exibido
    )

# View para cadastrar um novo usuário
def criarUsuario(request):
    # Verifica se o método da requisição é POST (envio do formulário)
    if request.method == 'POST':
        # Cria um formulário com os dados enviados (texto e imagem)
        form = UsuarioForm(request.POST, request.FILES)

        # POST: Campos de texto enviados pelo usuário
        # FILES: Arquivos enviados (como imagens)

        if form.is_valid():     # Verifica se os dados são válidos
            form.save()         # Salva o novo usuário no banco de dados
            return redirect('/usuario/login')  # Redireciona para a tela de login após o cadastro

    else:
        # Se a requisição for GET, ou seja, só para exibir a página
        form = UsuarioForm()    # Cria um formulário em branco

    # Renderiza o formulário na página de cadastro
    return render(
        request,                # Requisição recebida
        'cadastro.html',        # Página HTML a ser exibida
        {'form': form}          # Envia o formulário para o template
    )


