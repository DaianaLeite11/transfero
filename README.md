# 🚀 Transfero - Backend: Aula 1

Bem-vindo ao repositório da primeira aula do módulo de backend do projeto **Transfero**. Este projeto está em construção e visa fornecer uma base sólida para o desenvolvimento de APIs RESTful utilizando Python, Django e Django REST Framework.

## 🚧 Status do Projeto

Este projeto está em andamento. Atualmente, estamos implementando funcionalidades essenciais para a construção de uma API robusta e segura.


## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação de alto nível, conhecida por sua simplicidade e legibilidade.
- **Django**: Framework web para Python que facilita o desenvolvimento de aplicações web seguras e escaláveis.
- **Django REST Framework**: Conjunto de ferramentas poderosas e flexíveis para construir APIs Web em Django.
- **SQLite**: Banco de dados relacional leve, utilizado por padrão no Django para desenvolvimento e testes.

## 📌 Funcionalidades Implementadas

- **CRUD de Categorias**: Endpoints para criação, leitura, atualização e exclusão de categorias.
- **Autenticação JWT**: Geração e validação de tokens JWT para autenticação de usuários.

## 🚀 Como Rodar o Projeto 

 Para rodar este projeto em sua máquina local, siga os passos abaixo: 

 ### 1. Clone o repositório

 ```bash git clone https://github.com/DaianaLeite11/transfero.git cd transfero/backend/aula1 ``` 

 ### 2. Crie e ative um ambiente virtual

  No Windows: ```bash python -m venv venv .\venv\Scripts\activate ``` 
  No macOS/Linux: ```bash python3 -m venv venv source venv/bin/activate ``` 

 ### 3. Instale as dependências 
 ```bash pip install -r requirements.txt ``` 

### 4. Aplique as migrações do banco de dados 
```bash python manage.py migrate ``` 

### 5. Crie um superusuário para acessar o painel administrativo 
```bash python manage.py createsuperuser ``` 
Siga as instruções para definir o nome de usuário, e-mail e senha. 

### 6. Inicie o servidor de desenvolvimento
   ```bash python manage.py runserver ``` 

O servidor estará rodando em [http://localhost:8000](http://localhost:8000). 

### 7. Acesse o painel administrativo
 Para acessar o painel administrativo do Django, vá para [http://localhost:8000/admin](http://localhost:8000/admin) e faça login com o superusuário criado anteriormente. 

### 8. Teste a API
 Você pode testar os endpoints da API utilizando ferramentas como:
  [Postman](https://www.postman.com/) 
  [Insomnia](https://insomnia.rest/), fazendo requisições para [http://localhost:8000/api/](http://localhost:8000/api/). 

⚠️ **Nota**: Este projeto utiliza o banco de dados SQLite por padrão, que é adequado para desenvolvimento e testes. Para ambientes de produção, considere configurar um banco de dados mais robusto, como PostgreSQL ou MySQL. 


## 🧪 Testes
 Para garantir a qualidade e estabilidade da API, este projeto utiliza o framework de testes integrado do Django, juntamente com o Django REST Framework.


## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


Para adicionar este arquivo ao seu repositório no GitHub:

1. No seu repositório, clique em **Add file** e selecione **Create new file**.
2. No campo **Name your file**, digite `README.md`.
3. No editor, cole o conteúdo acima.
4. Role para baixo e clique em **Commit new file**.

Se precisar de mais alguma personalização ou ajuda, estou à disposição!
::contentReference[oaicite:0]{index=0}

## 📂 Estrutura do Projeto
```bash
📦 transfero
┣ 📂 backend
┃ ┗ 📂 aula1
┃ ┃ ┣ 📂 core
┃ ┃ ┃ ┣ 📂 migrations
┃ ┃ ┃ ┣ 📄 init.py
┃ ┃ ┃ ┣ 📄 admin.py
┃ ┃ ┃ ┣ 📄 apps.py
┃ ┃ ┃ ┣ 📄 models.py
┃ ┃ ┃ ┣ 📄 serializers.py
┃ ┃ ┃ ┣ 📄 tests.py
┃ ┃ ┃ ┣ 📄 urls.py
┃ ┃ ┃ ┣ 📄 views.py
┃ ┃ ┣ 📂 transfero
┃ ┃ ┃ ┣ 📄 init.py
┃ ┃ ┃ ┣ 📄 settings.py
┃ ┃ ┃ ┣ 📄 urls.py
┃ ┃ ┃ ┣ 📄 wsgi.py
┃ ┃ ┣ 📄 manage.py
┃ ┃ ┣ 📄 requirements.txt
┃ ┃ ┗ 📄 README.md

- **core**: Aplicativo principal que contém os modelos de dados, views, serializadores e URLs.
- **transfero**: Diretório do projeto Django que contém as configurações principais.
- **manage.py**: Script para interagir com o projeto Django (migrações, servidor de desenvolvimento, etc.).``` 


 





