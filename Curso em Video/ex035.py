print('Verifique se você foi aprovado ou não!')

nota = float(input('Digite a sua nota aqui: '))

if nota <= 5:
    print('Você tirou nota {} está abaixo da média, REPROVADO!'.format(nota))
elif nota >= 5.1 and nota <= 6.9:
    print('Você tirou a nota {} esta de RECUPERAÇÃO!'.format(nota))
elif nota >= 7:
    print('Parabéns sua nota foi {},você está APROVADO!'.format(nota))
else:
    print('Valor invalido, por favor verifique sua resposta!')
