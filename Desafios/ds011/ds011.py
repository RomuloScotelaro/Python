l=float(input('Informe a largura da parede:'))
a=float(input('Informe a altura da parade:'))
q=l*a
print('Sua parede tem dimesão {}x{} e sua área é de {:.2f}m².'.format(l,a,q))
print('Para pintar essa parede, você preicsará de {:.2f}l'.format(q/2))