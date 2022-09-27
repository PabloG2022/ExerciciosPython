#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    try:
      numero = int(input("digite um valor de 0 a 10: "))
    except ValueError:
      print('deve ser fornecido um valor inteiro')
    else:
      if 0<= numero <=10:
        print(f'número informado é: {numero}')
        break
      else:
        print('o numero deve estar entre zero e 10')