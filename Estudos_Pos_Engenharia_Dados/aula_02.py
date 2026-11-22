#Fiz a importação para usar o SQRT 
from math import sqrt as r

print("Codigo para resolução de formula de Bhaskara")

a = float(input("Digite o valor do primeiro coeficiente a: "))
b = float(input("Digite o valor do segundo coeficiente b: "))   
c = float(input("Digite o valor do terceiro coeficiente c: "))
#Tentei usar um verificador para caso não inserir um numero negativo na raiz 
if a == 0:
    print("O valor do coeficiente a não pode ser zero")
else:
    #Calculos da formula de Bhaskara
    delta = (b**2) -4 * a * c
    if delta < 0:
        print("A equação não possui raízes reais.")
    else:    
    

        x1 = ((-(b) + (r(delta)))/(2*a))
        x2 = ((-(b) - (r(delta)))/(2*a))
        #Resultados 
        print("O valor de delta é",(delta),"." )
        print("O Valor de X1 é", (x1), ".") 
        print("O Valor de X2 é", (x2), ".")