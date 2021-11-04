#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

from time import sleep
print('-='*20)
print('Analisador de triângulos.')
print('-='*20)
sleep(2)
print('Digite na sequência os segmentos (medidas) para análise...')
sleep(2)
print('-='*20)
r1 = float(input('Primeiro segmento: '))
print('-='*20)
sleep(2)
r2 = float(input('Segundo segmento: '))
print('-='*20)
sleep(2)
r3 = float(input('Terceiro segmento: '))
print('-='*20)
print('Estamos analisando os segmentos/medidas... Por favor, aguarde um instante.')
print('-='*20)
sleep(4)
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')
