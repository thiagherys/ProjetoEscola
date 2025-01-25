from class_aluno import Aluno, grupodealunos
from class_turma import Turma, turmas, turma_a, turma_b
import os

def mostrar_opcoes():
    print('''   
𝕆𝕡𝕔̧𝕠̃𝕖𝕤     
    1: Exibir turmas
    2: Matricular aluno
    3: Transferir aluno
    4: Ver alunos da turma     
          ''')

def escolher_funcao():
    opcaoescolhida = input('Digite o número da opção')
    if opcaoescolhida == '1':
        mostrar_turmas()
    elif opcaoescolhida == '2':
        matricular_aluno()
    input()
    
def mostrar_turmas():
    for turma in turmas:
        print(turma)
    input()

def matricular_aluno():
    nome = input('Qual o nome do aluno? ')
    idade = int(input('Qual a idade do aluno? '))
    nota1 = float(input('Qual a nota da primeira avaliação? '))
    nota2 = float(input('Qual a nota da segunda avaliação? '))
    novoaluno = Aluno(nome, idade, nota1, nota2)
    turmadesejada = input('qual turma você deseja matricular o aluno: turma_a ou turma_b? ')
    if turmadesejada == 'turma_a ':
        turma_a.adicionar_aluno(novoaluno)
    else:
        turma_b.adicionar_aluno(novoaluno)
    print(f'O aluno {novoaluno} foi adicionado a {turmadesejada} com sucesso')
    input()

def ver_alunos():
    turma_escolhida = input('Qual turma você gostaria de consultar os alunos turma_a ou turma_b ?')
    if turma_escolhida == 'turma_a':
        print('Alunos Prof. Anthony:')
        turma_a.listar_alunos()
    else:
        print('Alunos Prof. Robert:')
        turma_b.listar_alunos()
    input()
#def transferir_aluno():

def main():
    mostrar_opcoes()
    escolher_funcao()