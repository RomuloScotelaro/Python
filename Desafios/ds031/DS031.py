km =float(input('Qual é a distância da sua viagem? '))

if km <= 200:
    print('Você está prestes a começar uma viagem  de {}km.'.format(km))
    print('E o preço da sua passagem será de R${}'.format(km*0.50))
else:
    print('Você está prestes a começar uma viagem de {}km'.format(km))
    print('E o preço da sua passagem será de R${}'.format(km*0.45))