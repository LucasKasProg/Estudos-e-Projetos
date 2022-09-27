print('Descubra se você ja tem idade para servir o exercito!')

idade = int(input('Digite sua idade aqui: '))

menor = 18 - idade
maior = idade - 18

if idade <= 17:
    print('Você ainda nao tem idade para servir! Ainda falta(m) {} ano(s) para você poder servir!' .format(menor))
elif idade == 18:
    print('Já esta na hora de se alistar!')
elif idade > 18:
    print('Já passou da hora de se alistar! Já faz(em) {} ano(s) que você deveria ter se alistado!'.format(maior))