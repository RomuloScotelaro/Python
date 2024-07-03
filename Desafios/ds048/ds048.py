s =  0
c =  0
for r in range (1,501,2):
    if r % 3 == 0:
        s += r
        c += 1


print('A soma de todos os {} valores solicitados é {}'.format(c,s))