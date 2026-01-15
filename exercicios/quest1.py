## Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B e mostre se a soma é menor que C

a = int(input("Digite o primeiro número para o exercício 1: "))
b = int(input("Digite o segundo número para o exercício 1: "))
c = int(input("Digite o terceiro número para o exercício 1: "))

if ((soma := a + b) > c):
    print(soma, ">", c)
elif ((soma := a + b) == c):
    print(soma, ' = ', c)
else:
    print(c , " > ", soma)