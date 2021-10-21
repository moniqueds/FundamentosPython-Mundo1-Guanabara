medida = float(input('Informe uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A distância de {} m  corresponde a {:.2f} cm e {:.2f} mm'.format(medida, cm, mm))

# {:.2f} significa que terá 2 casas após a vírgula [que é o "ponto" > . < , se quiser ter, basta alterar de 0 para quantas você desejar.