from datetime import date
atual = date.today().year
ano = int(input('Informe o ano de nascimento: '))
idade = atual-ano

if idade <= 9:
   print('O atleta é mirim')

elif idade <= 14:
    print('O atleta é infantil')

elif idade <= 19:
    print('O atleta é junior')

elif idade <= 25:
    print('O atleta é senior')
else:
    print('O atleta é master')
