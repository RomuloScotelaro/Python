import math
an = float (input('Digite o âgulo que você deseja : '))
seno = math.sin(math.radians(an))
print ('O angulo de {} tem o SENO de {:.2f}'.format (an, seno))
cosseno = math.cos(math.radians(an))
print('O âgulo de {} tem o cosseno de {:.2f}'.format(an,cosseno))
tangente = math.tan(math.radians(an))
print('O angulo de {} tem  a TAGENTE de {:.2f}'.format(an,tangente))