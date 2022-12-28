print('{:=^25}'.format('Desafio 53'))
# Crie um programa que leia uma frase qualque e informe se ela é um palindromo desconsiderando os espaços
frase = str(input('Digite uma frase qualquer-> ')).strip()
# eliminei os espaços da frase
frase = ''.join(frase.split())
tam = len(frase)
# pega a frase inversa
aux = 0
rev = 'frase inversa'
# verifica se o inverso é igual a frase digitada
if frase == rev:
    print('A sua frase é um palindromo')
else:
    print('A sua frase não é um palindromo')
