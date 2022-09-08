import random

print('Sorteio para decidir quem limpara o quadro!')
p1 = input('Digite o nome do primeiro aluno a partipar do sorteio:')
p2 = input('Digite o nome do segundo aluno a partipar do sorteio:')
p3 = input('Digite o nome do terceiro aluno a partipar do sorteio:')
p4 = input('Digite o nome do quarto aluno a partipar do sorteio:')

lista = [p1, p2, p3, p4]

escolhido = random.choice(lista)

print('O escolhido para limpar o quadro foi {}!'.format(escolhido))
