n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:1f}'.format(n1,n2,media))
if 7 > media >= 6:
    print('O aluno esta APROVADO.')
elif media < 5:
    print('O aluno está RECUPERAÇÃO.')
else:
    print('O aluno esta REPROVADO')