km=float(input('Informe a quantidade de kms percorridos'))
dias=float(input('Informe a quantidade de dias alugados'))
valor=(km*0.15)+(dias*60)
print('O total do custo foi R${:.2f}'.format(valor))