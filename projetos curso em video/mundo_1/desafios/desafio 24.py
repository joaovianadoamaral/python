print('{:=^25}'.format('Desafio24'))
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'
cidade = str(input('Digite o nome da sua cidade --> '))
aux = cidade.split()
print('A sua cidade começa com a palavra Santo: {}'.format('Santo' in aux[0]))
