peso = float (input('Informe seu peso: '))
altura = float (input('Informe sua altura: '))
IMC = (peso)/(altura**2)
print ('Seu IMC é {:.1f}'.format(IMC))
if  IMC < 18.5:
    print('Seu IMC é abaixo do peso')
elif   18.5 <= IMC < 25:
    print('Seu IMC é Peso ideal')
elif 25 <= IMC < 30:
    print('Seu IMC é Sobrepeso')
elif 30 <= IMC < 40:
    print('Seu IMC é Obesidade')
elif IMC >= 40:
    print('Seu IMC é Obesidade mórbida')