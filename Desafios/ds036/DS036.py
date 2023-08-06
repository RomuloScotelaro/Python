print('--------------------------------------------------------------')
print('------------------PROGRAMA DE EMPRESTIMOS---------------------')
print('--------------------------------------------------------------')
casa = float(input('Qual valor da casa? R$'))
salario = float(input('Qual valor do seu sálario? R$'))
Ano = int(input('Qual tempo prentende pagar? ' ))
mes = (Ano * 12)
parcela = (casa/mes)
trava = salario*35/100

if  trava <= parcela:
    print('Voce não tem condições para o financiamento')
else:
    print('Seu financiamento foi aporvado a pacela sera de R${:.2f}, pago em {}, em uma casa no valor de {}'.format(parcela,mes,casa ))


