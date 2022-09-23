dis = int(input('Qual a distância em Km da sua viagem? '))

pre1 = dis * 0.5

pre2 = dis * 0.45

if dis <= 200:
    print('Sua viagem percorrera {}Km, o valor da passagem sera de R${}' .format(dis, pre1))
else:
    print('Sua viagem percorrera {}Km, o valor da passagem sera de R${}' . format(dis, pre2))