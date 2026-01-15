## Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo

a = int(input("Digite o primeiro número para o exercício 2: "));

if ((a % 2 == 0) and (a > 0)) :
    print(a , "é um número par e positivo.");
elif ((a % 2 == 0) and (a < 0)):
    print(a , "é um número par e negativo.");
elif ((a % 2 == 1) and (a > 0)):
    print(a , "é um número ímpar e positivo.");
elif ((a % 2 == 1) and (a < 0)):
    print(a , "é um número ímpar e negativo.");
else:
    print('É igual a 0')