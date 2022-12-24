print('{=^25}'.format('Desafio26'))
"""
faça um programa que leia uma frase pelo teclado e mostre:
*Quantas vezes aparece a letra 'a'
*Em que posição ela aparece pela primeira vez
*Em que posição ela parece da ultima vez
"""
frase = str(input('Digite uma frase -> '))
cont_a = frase.count('a')
pri_a = frase.find('a')
ult_a = 