vel = int(input('Qual a velocidade que o carro estava?'))

multa = (vel - 80) * 7
if vel > 80:
    print('Você utrapassou o limite de velocidade, você devera pagar uma multa de R$7,00 por Km acima do permitido')
    print('Você estava a {}Km/h, a sua multa sera R${}!' .format(vel, multa))
else:
    print('Você estava na velocidade permitida, pode prosseguir!')
