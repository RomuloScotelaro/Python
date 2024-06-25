print ('-='*20)
print ('Analisador de Triângulos')
print ('-='*20)
r1 = float (input('Informe a primeira reta: '))
r2 = float (input('Informe a segunda reta: '))
r3 = float (input('Informe a Terceira reta: '))
if r1 + r2 > r3 or r3 + r1 > r2 or r2 + r3 > r1:

    print('As retas PODEM FORMAR triangulo!', end='')
    if r1== r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 !=r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('As retas NÃO FORMAM triangulo')