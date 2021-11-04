#Faça um programa que leia três números e mostre qual é maior e qual é o menor.

from time import sleep
print('Você irá informar 3 números a seguir...')
sleep(2)
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
print('Analisando o menor...')
sleep(3)
#Verificar quem é o menor número
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('o menor valor digitado foi {}.'.format(menor))
print('Analisando o maior...')
sleep(4)
#Verificar quem é o maior número
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor digitado foi {}.'.format(maior))

