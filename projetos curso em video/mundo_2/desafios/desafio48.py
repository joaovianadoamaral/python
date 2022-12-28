print('{:=^25}'.format('Desafio 48'))
#faça um programa que calcule a soma entre todos os impares multiplo de 3, entre 1 e 500
soma = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
print('A soma anterior é igual a: {}'.format(soma))
