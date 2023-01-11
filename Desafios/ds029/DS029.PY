v = int(input('Qual velocidade atual do carro? '))
if v <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    m = v-80
    print("MULTADO! Você excdeeu o limite permetido que é 80km/h Você deve pagar uma multa de R${}!".format(m*7))
    print('Tenha mais cuidado! E dirija com segurança!')