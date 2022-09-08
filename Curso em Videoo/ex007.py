nome = input('Qual o nome do aluno? ')
n1 = int(input('Qual a primeira nota do(a) aluno {} ? '.format(nome)))
n2 = int(input('Qual a segunda nota do(a) aluno {} ? '.format(nome)))
media = (n1+n2) / 2
print('A media do(a) aluno {} é {}'.format(nome, media))

