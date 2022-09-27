print('Programa de classificação de atletas!')

idade = int(input('Digite sua idade aqui: '))

if idade <= 9:
    print('Você é um atleta MIRIM!')

elif idade <= 14:
    print('Você é um atleta INFANTIL!')

elif idade <= 19:
    print('Você é um atleta JUNIOR!')

elif idade <= 20: 
    print('Você é um atleta SÊNIOR!')

elif idade >= 21:
    print('Você é um atleta MASTER!')
    

