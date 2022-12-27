print('{:=^25}'.format('Desafio36'))
"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa vai perguntar o valor da Casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o Valor da prestação mensal, sabendo que ela não pode exceder 30% do salário senão o emprestimo será negado
"""
salario = float(input('Qual o seu salário? '))
temp = float(input('Em quanto tempo você irá pagar? '))
casa = float(input('Qual o valor da casa? '))
#valor da casa divido pela quantidade de meses
mensalidade = casa/(temp*12)
if mensalidade <= .3*salario:
    print('{}Parabens!!, o empréstimo foi aprovado{}'.format('\033[0;32m', '\033[m'))
else:
    print('{}O empréstimo foi recusado{}'.format('\033[0;31m', '\033[m'))
