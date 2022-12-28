print('{:=^25}'.format('Desafio 53'))
# Crie um programa que leia uma frase qualque e informe se ela é um palindromo desconsiderando os espaços
frase = str(input('Digite uma frase qualquer-> ')).strip()
frase = frase.split()
rev = frase #necessário uma definição prévia para não ocorrer erro
tam = len(frase)
#pega a frase inversa
aux = 0
print(rev)
print(frase)
print(tam)
