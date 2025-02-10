'''
# Exercitando…

## **🔹 Exercício Bônus 💡**

### **Simulação de Senha de Banco 🔐**

💡 **Enunciado**:

Crie um sistema que peça para o usuário digitar uma senha para acessar sua conta bancária. Ele tem **apenas 3 tentativas** para acertar a senha correta. Se ele errar as 3 vezes, o sistema bloqueia a conta.

📝 **Regras:**

- A senha correta é `"1234"`.
- O usuário tem **até 3 tentativas** para acertar.
- Se errar as 3 vezes, exiba "🚫 Conta bloqueada!".

'''
senha = ""
tentativa = 3
while senha.lower() != "1234" and tentativa > 0:
    senha = input("Digite sua senha: ")
    if senha.lower() != "1234":
        print("🚫 Senha incorreta!")
        tentativa -=1
        if tentativa == 0:
            print("🚫 Conta bloqueada!")
    else:
        print("na conta")


# if senha.lower() != "1234":
#     senha = input("Digite sua senha: ")    

# elif senha.lower() == "1234":
#         print("na conta")
# else:
#         print("erro inesperado")

  