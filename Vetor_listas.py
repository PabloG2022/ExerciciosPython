#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []

for _ in range(5):
  numero = float(input('Digite um número: '))
  lista.append(numero)

print(lista)