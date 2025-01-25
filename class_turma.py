from class_aluno import Aluno, grupodealunos

class Turma:
    def __init__(self, curso, professor):
        self.curso = curso
        self.professor = professor
        self.alunos = []

    def __str__(self):
        return f'{self.curso.ljust(20)} | {self.professor.ljust(20)}'
    
    def adicionar_aluno(self, *alunos):
        self.alunos.extend(alunos)

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno matriculado nesta turma.")
        for aluno in self.alunos:
            print(aluno)  # This will call the __str__ method of the Aluno class

turma_a = Turma('Inglês', 'Teacher Anthony')
turma_b = Turma('Tecnologia', 'Prof. Robert')

turmas = [turma_a, turma_b]

turma_a.adicionar_aluno(*grupodealunos[:5])
turma_b.adicionar_aluno(*grupodealunos[5:])