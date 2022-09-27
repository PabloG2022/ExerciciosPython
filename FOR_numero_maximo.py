#Faça um programa que leia 5 números e informe o maior número.

maximo = float(input('digite um número: '))

for _ in range(4):
  maximo =max(maximo, float(input('digite um número: ')))
  print(f'o número máximo encontrado até agora é {maximo}')