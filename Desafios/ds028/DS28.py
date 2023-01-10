import random
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
r = int(input('Em que numero eu pensei? '))
lista = [0, 1, 2, 3, 4, 5]
n = random.choice(lista)
print('PROCESSANDO...')
if r == n:
    print('Você acertou, PARABENS!!!')
else:
    print('Você  errou tente novamente')
print('O numero foi {}'.format(n))