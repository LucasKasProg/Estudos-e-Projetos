print('Programa para verificar seu desconto!')

valor = int(input('Digite o valor do produto: '))

print('Escolha o modo de pagamento: ')

print('Tecle 1 para pagar com dinheiro ou cheque ganhando 10% de desconto!')
print('Tecle 2 para pagar com cartão de debito ganhando 5% de desconto!')
print('Tecle 3 para pagar com até em 2x no cartão sem desconto!')
print('Tecle 4 para pagar 3x ou mais com 20% de juros!')
opcao = int(input('Digite a opção desejada: '))

op1 = valor - (valor*10/100)

op2 = valor - (valor*5/100)

op3 = valor

op4 = valor + (valor*20/100)

if opcao == 1:
    print('Você escolheu pagar no dinheiro, o valor do seu produto é R${} com o desconto de 10% você ira pagar R${}'.format(valor, op1))
elif opcao == 2:
    print('Você escolheu pagar no debito, o valor do seu produto é R${} com o desconto de 5% você ira pagar R${}'.format(valor, op2))
elif opcao == 3:
    print('Você escolheu pagar em até 2x no cartão, o valor do seu produto é R${} e nesse modo de pagamento na há desconto!'.format(valor))
elif opcao == 4:
    print('Você escolheu pagar parcelado em x3 ou mais no cartão, o valor do seu produto é R${} com o juros de 20% você ira pagar R${}'.format(valor, op4))


