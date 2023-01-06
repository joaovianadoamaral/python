# use ... ou pass para não precisar escrever o código.

#não é recomendado fazer conversões direto no input já que não se pode verificar o que o usuário digitou
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

# quando se usa strings nomeadas, dela pra frente tem que nomear todas
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

# podemos usar a função format com indices sendo que para '{2}{1}{0}'.format(a,b,c)
# será printado na tela as variaveis na ordem : c b a. já que a possui o indice 0, b o indice 1, e c o indice 2
# quando é passado 3 argumentos no format(), não necessariamente se usará os 3.