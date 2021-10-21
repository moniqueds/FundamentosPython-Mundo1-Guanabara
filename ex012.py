preco = float(input('Informe o valor do produto: R$ '))
novo = preco - (preco * 5 / 100)
print('O valor do produto sem desconto era de R$ {:.2f}, mas com desconto de 5% irá custar R$ {}'.format(preco, novo))


#para calcular percentual precisa ser:
# 5/100 = 0.05
