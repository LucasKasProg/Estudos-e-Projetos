a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
#Verificando quem é menor!
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é maior!
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O menor número digitado foi {}'.format(menor))
print('O maior número digitado foi {}'.format(maior))