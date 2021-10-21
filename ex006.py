n = int(input('Informe um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O tripo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2F}'.format(n, (n*3), n, (n**(1/2))))

# outra forma de calcular

n = int(input('Informe um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O tripo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2F}'.format(n, (n*3), n, pow(n,(1/2))))

