n1 = float(input('Qual foi sua primeira nota?'))
n2 = float(input('Qual foi sua segunda nota?'))
media = (n1 + n2)/ 2
if media <= 6:
    print('Sua média foi {}, você está Reprovado!'.format(media))
else:
    print('Sua média foi {}, você está Aprovado!' .format(media))
    