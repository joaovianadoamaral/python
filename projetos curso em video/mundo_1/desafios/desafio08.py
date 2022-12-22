print('{:=^25}'.format('desafio08'))
#escreva um programa que leia o valor em metros, e converta para centimetros e milimetros
metro = float(input('digite o valor de medida em metros: '))
milimetro=metro*1000
centimetro=metro*100
print('{:.2f} metros é equivalente a:\n{:.2f} centimetros\n{:.2f} milimetros'.format(metro, centimetro, milimetro))
