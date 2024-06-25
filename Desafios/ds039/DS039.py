ano = int(input('Ano de nascimento: '))
ref = 2017
idade = ref-ano

print('Quem nasceu em {}, tem {}, anos em 2017'.format(ano,idade))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18-idade))
    print('Seu alistamento será {}'.format(ano+18))
elif idade > 18:
    print('Você já deveria ter se alistado {}'.format(idade-18))
    print('Seu alistamento foi {}'.format(ano+18))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')