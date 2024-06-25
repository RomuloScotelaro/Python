num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO 
[ 2 ] coverter para OCTAL 
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} covertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print( opcao == ('{} covertido para OCTAL é igual a {}'.format(num, oct(num)[2:])))
elif opcao == 3:
    print( opcao == ('{} covertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:])))
else:
    print('Opção ivalida. Tente novamente')
