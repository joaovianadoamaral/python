print('{:=^25}'.format('desafio11'))
#faça um programa que leia a largura e a altura de uma
#parede em metros, calcule a sua área e a quantidade de
#tinta necessária para pinta-la, sabendo que cada litro de tinta
#pinta uma área de 2m²
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area_parede = largura*altura
latas = area_parede/2
print('A quantidade necessária de tinta para pintar sua parede é : {:.2f}'.format(latas))
