## Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B e mostre se a soma é menor que C

a = int(input("Digite o primeiro número para o exercício 1: "));
b = int(input("Digite o segundo número para o exercício 1: "));
c = int(input("Digite o terceiro número para o exercício 1: "));

if ((soma := a + b) > c):
    print(soma, ">", c);
elif ((soma := a + b) == c):
    print(soma, ' = ', c)
else:
    print(c , " > ", soma);

## Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo

d = int(input("Digite o primeiro número para o exercício 2: "));

if ((d % 2 == 0) and (d > 0)) :
    print(d , "é um número par e positivo.");
elif ((d % 2 == 0) and (d < 0)):
    print(d , "é um número par e negativo.");
elif ((d % 2 == 1) and (d > 0)):
    print(d , "é um número ímpar e positivo.");
elif ((d % 2 == 1) and (d < 0)):
    print(d , "é um número ímpar e negativo.");
else:
    print('É igual a 0')