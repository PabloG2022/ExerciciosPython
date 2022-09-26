#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

N1 = int(input('digite a primeira nota: '))
N2 = int(input('digite a segunda nota: '))
media = (N1 + N2)/ 2
print(f'sua média foi de {media}')
if media >= 10:
  print('Aluno aprovado com distinção')
elif media >= 7:
  print('aluno aprovado')
else:
  print('aluno reprovado')