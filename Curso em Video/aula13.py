for c in range (0, 8,):
    print(c)

n = int(input('Digite um numero:'))

for cn in range (1, n+1):
    print(cn)

i = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passo: '))
for cm in range(i, f+1, p):
    print(cm)

s = 0
for cb in range (0,3):
    n1= int(input('Digite um número:'))
    s += n1
print('O somatório de todos os valores foi {}'.format(s))

print('fim')
