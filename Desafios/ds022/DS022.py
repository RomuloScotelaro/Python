nome = str(input("Digite seu nome completo:")).strip()
print('Analisando seu nome...')
print('Seu nome em maíscula é {}'.format(nome.upper()))
print ('Seu nome em letras minisculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {}'.format(nome.find(' ')))
#sepra = nome.split()
#print ('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
