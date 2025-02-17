
# comandos básicos do git

--> ``git config --global user.name "Mona Lisa"``
- inclui a credencial do seu nome

-->  `git config --global user.email "MonaLisa@gmail.com"`
- inclui a credencial do seu email

-->  ``git init ``
- inicializa o repositório

-->  ``git status ``
-  exibe se os arquivos/ pastas estão adicionados ao repositório

-->  ``git add nome do arquivo ``
-  adiciona o arquivo ao repositório local

-->  ``git add .``
-  adiciona todos os arquivos modoficados/criados ao repositório local

-->  ``git branch -M main``
- altera o nome da branch principal de master para main 

-->  ``git commit -m "mesagem de atualização"``
- cria um commit para que seja iniciado um novo versionamento.

-->  ``git log``
- lista todos os commits realizados

-->  ``git log --oneline --graph --decorate``
- forma compacta de exibir os commits

-->  ``git  remote add origin https://exemplo.com/repositorio``
- realiza a sincronização do repositório local com o remoto
 
 -->  ``git push - u origin main``
 - envia as informações do repositório local para o remoto

 -->  ``git clone``
 - clona um repositório

 -->  ``git branch``
 - exibe as branch que foram criadas

  -->  ``git branch nome_da_branch``
  - cria uma nova branch

-->  ``git checkout nome_da_branch``
- altera a branch selecionada
