s = 0
for _ in range (1,7):
    n = int(input('Informe um numero: '))
    if n % 2 == 0:
      s += n

print('A soma do valores pare é {}'.format(s))
