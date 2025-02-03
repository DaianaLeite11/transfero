nome_do_usuario = "William" #str
idade_do_usuario = 22 #number
cidade_do_usuario = "São Paulo" #str
CPF_DO_USUARIO = "14806445796" #const fake

# print(CPF_DO_USUARIO)
# CPF_DO_USUARIO = "1111111111"
# print(CPF_DO_USUARIO)

# print(nome_do_usuario)
# nome_do_usuario = "José" # redeclarou a variável
# print(nome_do_usuario)


# Concatenação Simples com + ou ,
# print("Olá, meu nome é " , nome_do_usuario)
# print("Olá, meu nome é " + nome_do_usuario + " e eu moro na cidade de " + cidade_do_usuario)


# Usando f-string
mensagem =  f'''
Olá, meu nome é {nome_do_usuario} 
e eu moro na cidade de {cidade_do_usuario} 
e tenho {idade_do_usuario}'''

print(mensagem)