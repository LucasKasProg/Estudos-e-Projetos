print('Programa para calcular números impares, mútiplos de três!')
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
        
print('A soma dos {} valores solicitados é de {}'.format(cont, soma))