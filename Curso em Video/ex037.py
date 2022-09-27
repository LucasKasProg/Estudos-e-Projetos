print('Programa para calcular o seu IMC!')

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura**2)

if imc <= 18.4:
    print('Seu IMC é de {:.2f}, você esta abaixo do peso!'.format(imc))
elif imc <= 25:
    print('Seu IMC é de {:.2f}, você esta com o peso ideial!'.format(imc))
elif imc <= 30:
    print('Seu IMC é de {:.2f}, você esta com sobrepeso!'.format(imc))
elif imc <= 40:
    print('Seu IMC é de {:.2f}, você esta com obsesidade!'.format(imc))
elif imc >= 40.0:
    print('Seu IMC é de {:.2f}, você esta com obsidade mórbita!'.format(imc))

