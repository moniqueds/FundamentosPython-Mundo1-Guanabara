# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
#Exemplo: Digite um número: 6.127.
# O número 6.127 tem a parte inteira 6.

#como eu resolvi
import math
num = float(input('1-Digite um número: '))
int = math.trunc(num)
print('O número {} tem a parte inteira {}'.format(num, int))

#como prof resolveu:
import math
num = float(input('2-Digite um número: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

#exemplo 2
from math import trunc
num = float(input('3-Digite um número: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

#exemplo 3
num = float(input('4-Digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
