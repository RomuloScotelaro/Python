a = int(input('Primeiro valor'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))

menor = a
if b < a and b < c:
    menor = b
if c < a and b > c:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if b > a and b > c:
    maior = c
