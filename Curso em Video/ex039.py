from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogador?'))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Jogador e computador jogaram igual, deu EMPATE!')
    elif jogador == 1:
        print('PAPEL ganha de PEDRA, jogador VENCEU!')
    elif jogador == 2:
        print('PEDRA ganha de TESOURA, a maquina VENCEU!')
    else:
        print('JOGADA INVALIDA!')

elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('PAPEL ganha de PEDRA, computador VENCEU!')
    elif jogador == 1:
        print('Jogador e computador jogaram igual, deu EMPATE!')
    elif jogador == 2:
        print('TESOURA ganha de PAPEL, jogador VENCEU!')
    else:
        print('JOGADA INVALIDA!')

elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('PEDRA ganha de TESOURA, jogador VENCEU!')
    elif jogador == 1:
        print('TESOURA ganha de PAPEL, computador VENCEU!')
    elif jogador == 2:
        print('Jogador e computador jogaram igual, deu EMPATE!')
    else:
        print('JOGADA INVALIDA!')

print('-=' * 11)