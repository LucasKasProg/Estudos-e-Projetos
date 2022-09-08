preço = float(input('Qual o valor do produto?'))
novo = preço - (preço*5/100)
print('O produto que custava R${} na promoção com desconto de 5% esta custando R${}  '.format(preço, novo))
