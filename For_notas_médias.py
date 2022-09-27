#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

notas = [10, 5.5, 7, 9]
tamanho = len(notas)
print(f'foram lidos {tamanho} notas')
print(' '.join([str(nota) for nota in notas]))
notas.reverse()

for nota in notas:
  print(nota)

soma = sum(notas)

print(f'soma das notas é: {soma}')

media = soma / tamanho

print(f'A média das notas é: {media}')

print('notas acima da média')

print(''.join([str(nota) for nota in notas if nota > media]))