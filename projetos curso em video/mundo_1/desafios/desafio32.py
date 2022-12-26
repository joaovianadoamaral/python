print('{:=^25}'.format('Desafio32'))
#peça ao usuário um ano e descubra se esse ano é bissexto
#esse ano tem que ser dividido por 4
ano = int(input('Digite um ano -> '))
bissexto = ano % 4
if bissexto == 0:
    print('Esse é um ano bissexto')
else:
    print('Esse não é um ano bissexto')
