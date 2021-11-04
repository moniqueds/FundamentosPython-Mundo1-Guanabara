# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$ 0,50 por KM, para viagens de até 200KM, e R$ 0,45 para viagens mais longas.

distância = int(input('Qual a distância da sua viagem em KM? '))
print('A distância total da sua viagem é {} Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('O valor da sua passagem será de R${:.2f}'.format(preço))

# Outra forma de calcular, simplifcado:

distância = int(input('Qual a distância da sua viagem em KM? '))
print('A distância total da sua viagem é {} Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('O valor da sua passagem será de R${:.2f}'.format(preço))
