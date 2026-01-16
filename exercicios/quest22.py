## Faça um algoritmo que leia dois valores inteiros A e B, imprima na tela o quociente e o resto da divisão inteira entre eles.

valor_a = int(input("Digite o valor de A: "))
valor_b = int(input("Digite o valor de B: "))

quociente = valor_a // valor_b
resto = valor_a % valor_b

print("O quociente da divisão entre A e B é: ", quociente)
print("O resto da divisão entre A e B é: ", resto)
