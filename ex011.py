largura = float(input('Informe a largura da sua parede em metros: '))
altura = float(input('Informe a altura da sua parede em metros: '))
area = largura * altura
print('Sua parede tem a dimensão de {} (largura) x {} (altura) e sua área é de {}m²'.format(largura, altura, area))
tinta = area / 2 # /2 pq a cada 1L pinta a area de 2m² (este calculo não é real, é apenas para exercício)
print('Para pintar esta parede, você precisará de {}L de tinta'.format(tinta))