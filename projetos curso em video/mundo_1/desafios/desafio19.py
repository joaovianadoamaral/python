from random import randint
print('{:=^25}'.format('Desafio19'))
#faça um programa que leia o nome de 4 alunos para que o professor sortei 1 e faça ele apagar o quadro
nome1 = input('Digite o nome do 1° aluno: ')
nome2 = input('Digite o nome do 2° aluno: ')
nome3 = input('Digite o nome do 3° aluno: ')
nome4 = input('Digite o nome do 4° aluno: ')
aux = randint(1,4)
print('O aluno {} foi escolhido: {}'.format(aux, nome1))
