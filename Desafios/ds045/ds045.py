import random
list = [0, 1, 2]
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
op = int(input('Qual é a sua jogada?'))
pc = (random.choice(list))
# PEDRA

if pc == 0 and op == 0:
    print('EMPATE')
elif pc == 0 and op == 1:
    print('JOGADOR VENCE')
elif pc == 0 and op == 2:
    print('MAQUINA VENCE')

# PAPEL

elif pc == 1 and op == 1:
    print('EMPATE')
elif pc == 1 and op ==  0:
    print('MAQUINA VENCE')
elif pc == 1 and op == 2:
    print('JOGADOR VENCE')

# TESOURA

elif pc == 2 and op == 2:
    print('EMPATE')
elif pc == 2 and op == 0:
    print('JOGADOR VENCE')
elif pc ==2 and op == 1:
    print('MAQUINA VENCE')
