# aluno -> nome, cpf, idade -> são atributos
# matricula (false ou true) -> são métodos
# a classe vai ser o molde
# o objto vai ser a cópia
# o padrão da classe é PascalCase

class Aluno:   

    def __init__(self,nome, cpf, idade):
         
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.matriculado = True

    def situacao(self):
        self.matriculado = False
    
    def exibirInfo(self):
        print(f"Nome do(a) aluno (a) é : {self.nome}")
        print(f"CPF do(a) aluno (a é): {self.cpf}")
        print(f"Idade do(a) aluno (a é): {self.idade}")
        print(f"Matriculado? {self.matriculado}")

a1= Aluno("jose", "123", 22)
a2 = Aluno("ana", "456", 21)


a1.exibirInfo() 
a2.exibirInfo()

a2.situacao()
a2.exibirInfo()

