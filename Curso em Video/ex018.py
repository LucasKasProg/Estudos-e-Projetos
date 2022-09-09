from math import cos, tan, sin, radians

an = float(input('Digite o ângulo que você deseja:'))

seno = math.sin(math.radians(an))

cosse = math.cos(math.radians(an))

tang = math.tan(math.radians(an))

print('O ângulo de {} tem o SENO de {:.2f}' .format(an, seno))

print('O ângulo de {} tem o COSSENO de {:.2f}' .format(an, cosse))

print('O ânguo de {} tem o TANGENTE de {:.2f}'.format(an, tang))

