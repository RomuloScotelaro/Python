salario = float(input('Informe o valor do seu salário? '))

if salario <= 1250.00:
    aumento = salario*15/100
    print ('Seu salário agora será R${:.2f} com o aumento'.format(salario+aumento))
else:
    aumento = salario*10/100
    print('Seu salário agora será R${:.2f} com o aumento'.format(salario+aumento))