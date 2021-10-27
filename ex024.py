#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = str(input('Informe o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')

# .strip para remover espaços indesejados
# .upper para colocar tudo maiúsculo, pois o usuário pode digitar de uma forma como "Santo", ou "sAntO", e aí não irá identificar.
# poderia ter colocado tudo pra minúsculo também (.lower)