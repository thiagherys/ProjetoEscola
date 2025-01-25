class Aluno:
    def __init__(self, nome, idade, nota1, nota2):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2

    def __str__(self):
        return (f'{self.nome.ljust(20)} | {str(self.idade).ljust(20)} anos | Media {str(self.media_bimestral).ljust(20)} | {self.aprovação.ljust(20)}')

    @property
    def media_bimestral(self):
        return (self.nota1 + self.nota2) / 2 
    
    @property
    def aprovação(self):
       return 'Aprovado' if self.media_bimestral > 6 else 'Reprovado'

#Alunos da turma
Aluno1 = Aluno("Thiago", 25, 7, 10)
Aluno2 = Aluno("Maria", 22, 8, 9)
Aluno3 = Aluno("João", 21, 6, 7)
Aluno4 = Aluno("Ana", 20, 5, 6)
Aluno5 = Aluno("Pedro", 23, 9, 9)
Aluno6 = Aluno("Lucas", 24, 10, 10)
Aluno7 = Aluno("Carlos", 26, 4, 5)
Aluno8 = Aluno("Bruna", 22, 6, 6)
Aluno9 = Aluno("Fernanda", 25, 7, 8)
Aluno10 = Aluno("Rafael", 27, 5, 7)

grupodealunos = [Aluno1, Aluno2, Aluno3, Aluno4, Aluno5, Aluno6, Aluno7, Aluno8, Aluno9, Aluno10]