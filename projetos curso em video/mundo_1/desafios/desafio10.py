print('{:=^25}'.format('desafio10'))
#Crie um programa que leia quantos reais ele têm na carteira e quantos dolares ela pode comprar
#Cotação do exercicio 1 dolar = 3.27 reais
reais = float(input('quantos reais você tem? '))
dolar= reais/3.27
print('Você consegue comprar {:.3f}US$'.format(dolar))
