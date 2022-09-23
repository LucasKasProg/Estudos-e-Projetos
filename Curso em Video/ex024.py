import random

print('O computador escolheu um numero entre 1 e 5!')
ne = int(input('Tente adivinhar qual numero foi escolhido:'))

lista = (1, 2, 3, 4, 5)
ns = random.choice(lista)

if ne == ns:
    print('Você acertou! o computador também escolheu o número {}.'.format(ns))
else:
    print('Errou! você escolheu o numero {}, o computador escolheu o numero {}! Não foi dessa vez, tente novamente xD'.format(ne, ns))
    



