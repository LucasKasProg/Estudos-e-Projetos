print('Bem vindo ao programa Minha Casa Minha Vida!')

vlr_casa = int(input('Qual o valor da casa que deseja simular a compra?'))
vlr_salario = int(input('Qual o valor do seu salário?'))
parcelas = int(input('Em quantas parcelas você pretende pagar?'))

vlr_parcela = vlr_casa // parcelas

if vlr_parcela >= (vlr_salario*30/100):
    print('Seu emprestimo foi negado pois o valor da parcela seria R${} e ultrapassa 30% do seu salário!'.format(vlr_parcela))
else:
        print('Seu emprestimo foi aprovado! Você pagará uma parcela de R${}, durante {}meses, parabéns!'.format(vlr_parcela, parcelas))