## Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são válidos
# determine se o triângulo é equilátero, isósceles ou escaleno.

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if (a == b and b == c):
    print("O triângulo é equilátero")
elif (a == b or b == c or a == c):
    print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno")