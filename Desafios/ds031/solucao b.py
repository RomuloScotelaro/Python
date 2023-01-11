ditancia = float(input('Qual é á distancia da sua viagem? '))
print('Você esta prestes a começar uma viagem?')
preco = ditancia * 0.50 if ditancia <= 200 else ditancia * 0.45
print('E o preço da sua passagem séra de R${:2.f}'.format(preco))