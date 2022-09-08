sla = float(input('Qual é o salario do Funcionário?'))
slnv = sla + (sla*15/100)
print('O salario deste funcionário que recebia R${}, com aumento de 15% agora recebe R${:.2f}'.format(sla, slnv))