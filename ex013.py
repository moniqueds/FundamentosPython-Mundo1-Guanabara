salario = float(input('Informe seu salário atual: R$ '))
novo = salario + (salario * 15 / 100)
print('O seu salário era de R$ {:.2f}, e com o aumento será de R$ {:.2f}'.format(salario, novo))

#:.2f para ter duas casas após a vírgula
# 15 / 100 = 15%