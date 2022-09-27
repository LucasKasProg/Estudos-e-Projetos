print('Bem vindo ao convertor de números!')
num = int(input('Digite um número:'))
print('Qual sera a base de converção?')
print('Digite 1 para converter para binário')
print('Digite 2 para converter para octal')
print('Digite 3 para converter para hexadecimal')
print('Digite 4 para todas as opções a cima!')
opçao = int(input(''))
binary = bin(num)
octal = oct(num)
hexa = hex(num)

if opçao == 1:
   print('O número {} convertido para binário é {}.'.format(num, binary))
elif opçao == 2:
   print('O número {} convertido para octal é {}.'.format(num, octal))
elif opçao == 3:
    print('O número {} convertido para hexadecimal é {}.'.format(num, hexa))
elif opçao == 4:
    print('O número {} convertido para binário é {}.'.format(num, binary))
    print('O número {} convertido para octal é {}.'.format(num, octal))
    print('O número {} convertido para hexadecimal é {}.'.format(num, hexa))
else:
    print('Opção invalida, tente novamente!')

