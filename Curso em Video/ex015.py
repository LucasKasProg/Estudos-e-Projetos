dias = float(input('Quantos dias você ficou com o carro?'))
km = float(input('Quantos Kms você percorreu?'))
valor = (dias * 60) + (km * 0.15)
print('O valor total a ser pago é de R${:.2f}'.format(valor))