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