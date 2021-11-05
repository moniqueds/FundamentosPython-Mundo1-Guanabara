
print("\033[0;30;41mOlá, Mundo!\033[m")
print('\033[4;33;44mOlá, Mundo!\033[m')
print('\033[1;35;43mOlá, Mundo!\033[m')
print('\033[30;42mOlá, Mundo!\033[m')
print('\033[mOlá, Mundo!\033[m')
print('\033[7:30m\033[m')

# OUTRO EXEMPLO
nome = 'Monique'
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

#OUTRO EXEMPLO 2: Cria lista de cores, com seus nomes, e depois só informa após o format.
# 1º {} inicia cor, 2º {} é o texto e 3º é o fim da cor.

nome = 'Monique'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))