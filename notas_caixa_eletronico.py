#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = 299
notas_de_100 = notas_de_50 = notas_de_10 = notas_de_5 = notas_de_1 = 0

notas_de_100, saque = divmod(saque, 100)

notas_de_50, saque = divmod(saque, 50)

notas_de_10, saque = divmod(saque, 10)

notas_de_5, notas_de_1 = divmod(saque, 5)

if notas_de_100 > 0:
  print(f'{notas_de_100} nota(s) de 100')

if notas_de_50 > 0:
  print(f'{notas_de_50} nota(s) de 50')

if notas_de_10 > 0:
  print(f'{notas_de_10} nota(s) de 10')

if notas_de_5 > 0:
  print(f'{notas_de_5} nota(s) de 5')

if notas_de_1 > 0:
  print(f'{notas_de_1} nota(s) de 1')