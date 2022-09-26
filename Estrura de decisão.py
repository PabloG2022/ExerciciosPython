#Faça um Programa que verifique se uma letra digitada
# é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

Letra = input("digite o sexo M/F: ")
if Letra == 'M'or Letra == 'm':
  print('sexo masculino')
elif Letra == 'F' or Letra == 'f':
  print('sexo feminino')
else:
  print('sexo inválido')