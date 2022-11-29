v=float(input('Qual é o preço do produto? :R$'))
d=v*5/100
print('O produto que custava R${}, na promoção com desconto de 5% vai custar {:.2f}'.format(v,(v-d)))