peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
IMC = (peso)/(altura**2)
print ('Seu IMC é {:.1f}'.format(IMC))
if  IMC < 18.5:
    print('Seu IMC é abaixo do peso')
elif IMC >= 18.5 and IMC < 25:
    print('Seu IMC é Peso ideal')
elif IMC >= 25 and IMC <= 30:
    print('Seu IMC é Sobrepeso')
elif IMC >= 30 and IMC <= 40:
    print('Seu IMC é Obesidade')
elif IMC >= 40:
    print('Seu IMC é Obesidade mórbida')