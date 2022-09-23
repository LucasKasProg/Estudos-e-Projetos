sal = int(input('Qual o valor do seu salário?'))

sal10 = sal + (sal*10/100)
sal15 = sal + (sal*15/100)

if sal >= 1250:
    print('Seu salário era de R${}, com o reajuste de 10% agora você recebe R${}!'.format(sal, sal10))
else:
    print('Seu salário era de R${}, com o reajuste de 15% agora você recebe R${}!' .format(sal, sal15))

    