print('=' *20)
print('10 TERMOS DE UMA PA')
print('=' *20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
val = razao * 10
soma = 0
for c in range(termo, val ,razao):
    print('{} '.format(c),end='-> ')
print('ACABOU!')

