## Faça um algoritmo que receba um valor A e B, e troque o valor de A por B e o valor de B por A e imprima na tela os valores.

numA = int(input("Digite o primeiro número: "))
numB = int(input("Digite o segundo número: "))

## uso de tuplas temporárias
(numA , numB) = (numB , numA)

print("O valor de A é : ",numA, " e o valor de B é: ", numB)


