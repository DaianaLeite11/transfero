def saudacao():
    print("Hello word!")

#chamando a função
    
saudacao() #ou

def entrada(nome): # nome é um parametro
    print(f"Olá, {nome}! Seja bem-vindo!")

# entrada("William")
# entrada("Ana")
# entrada("Bia")
# entrada("Liz")

def soma(a,b):
    somar = a + b
    return somar

print(soma(10,20))
print(soma(15,10) )
print(soma (10,2))

def identificacao(nome, idade):
    print(f"Olá, {nome}! \nSua idade é {idade} anos.")

identificacao("William", 22)

# Função Nomeadas
def apresentar(nome= "visitante"):
    print(f"Olá, {nome}!, Seja bem-vindo!")

apresentar()
apresentar("Ana")

# funçao com retorno de multiplos valores

def calcular_area_perimetro(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

print(calcular_area_perimetro(4,2))


def contagem_regressiva(n):
    while n > 0:
        print(n)
        n -= 1
    print("❌")

contagem_regressiva(5)


#Exemplo: Função com for (loop)

def listar_nomes(nomes):
    for nome in nomes:
