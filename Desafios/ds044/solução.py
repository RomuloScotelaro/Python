print('='*20)
print('CAIXA')
print('='*20)
valor = float(input('Preço das Compras: R$'))
print('''FORMAS DE PAGAMENTO:
        [1] à vista dinheiro/cheque
        [2] à vista cartão
        [3] 2x no cartão
        [4] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))
if op == 1:
    total = valor - (valor*10/100)
    print('Sua compra de R${:.2F} vai custar R${:.2F}'.format(valor,total))

elif op == 2:
    total = valor - (valor*5/100)
    print('Sua compra de R${:.2F} vai custar R${:.2F}'.format(valor,total))
elif op == 3:
    parcela = valor/2
    print('Sua compra de R${:.2F} suas parcelas vão custar R${:.2F}'.format(valor,parcela))
elif op == 4:
    total = valor + (valor*20/100)
    parcela = int(input('Informe a quantidade de pacelas: '))
    totalc = total/parcela
    print('Sua compra de R${:.2F} suas parcelas vão custar R${:.2F}'.format(valor, totalc))

else:
    total = 0
    print('Opção invalida informe uma opção correta ')