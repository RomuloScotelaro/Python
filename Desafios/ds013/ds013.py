salario=float(input('Qual é o salário do funcionario? R$'))
aumento=salario*15/100+salario
print('Um funcionario que ganhava R${:.2F}, com 15%, de aumento, pasa a receber R${:.2F}'.format(salario,aumento))