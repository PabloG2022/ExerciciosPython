#Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = 'Pablo Guilherme da Silva'.upper()

nome_invertido_por_letras = ''.join(reversed(nome))

nome_invertido_por_palavras = ' '.join(reversed(nome.split()))

print(f'nome com letras em maiscúlos: {nome}')
print(f'nome com letras maiúsculas invertido por letras: {nome_invertido_por_letras}')
print(f'nome com letras maiúsculas invertido por palavras: {nome_invertido_por_palavras}')